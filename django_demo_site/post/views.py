from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count
from django.template.defaultfilters import slugify
from taggit.models import Tag
from unidecode import unidecode

from post.models import Post, Comment
from post.forms import PostForm, CommentForm


def root_view(request):
    return HttpResponse(r'<a href="/post"> '
                        r'<h1 align="center"  style="font-size:80px">Qilin Garden</h1> '
                        r'</a>'
                        r'<p style="text-align:center; font:16pt; courier; color:blue">' 
                        r'A Python and Django powered website.'
                        r'</p>')


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    # 3 posts in each page
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/list.html', {'page': page,
                                              'posts': posts,
                                              'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by(
        '-same_tags', '-publish')[:4]

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        print(request.user)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(request.path)
    else:
        comment_form = CommentForm()
        return render(request, 'post/detail.html', {'post': post,
                                                    'comments': comments,
                                                    'comment_form': comment_form,
                                                    'similar_posts': similar_posts})


def post_new(request):
    if request.method == "POST":
        # save the post form
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(unidecode(new_post.title))
            new_post.author = request.user
            new_post.status = 'published'
            new_post.save()
            return HttpResponseRedirect('/post')
        else:
            print("invalid form")
            return render(request, 'post/new_post.html', {'form': form})
    else:
        # display the post form
        form = PostForm()
        return render(request, 'post/new_post.html', {'form': form})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/list.html'

