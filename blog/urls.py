from django.conf.urls import url

from blog.views.base import BaseView

urlpatterns = [
    url(r'^$', BaseView.as_view(), name='base'),
]
