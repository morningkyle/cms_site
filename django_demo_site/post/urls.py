from django.conf.urls import url
from post import views


urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new$', views.post_new, name='post_new'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    #url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]


