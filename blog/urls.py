from django.conf.urls import url

from blog.views.blog_feed import BlogFeedView
from blog.views.blog_post import BlogPostView
from blog.views.contact import ContactView
from blog.views.homepage import HomepageView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^blog/(?P<slug>[-\w]+)/$', BlogPostView.as_view(), name="blog-post"),
    url(r'^blog/$', BlogFeedView.as_view(), name="blog-feed"),
    url(r'^contact/$', ContactView.as_view(), name="contact")
]
