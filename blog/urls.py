from django.conf.urls import url

from blog.views.homepage import HomepageView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
]
