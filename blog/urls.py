from django.conf.urls import url

from blog.views.homepage import HomepageView
from blog.views.blogpost import BlogPostView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^blog/(?P<slug>[-\w]+)/$', BlogPostView.as_view(), name="blog-post")
]
