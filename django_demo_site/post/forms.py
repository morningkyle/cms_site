from django import forms

from post.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['style'] = 'width:60%;'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
