from django.http import HttpResponse
from django.urls import reverse

from django.views.generic import TemplateView


PAGES = [
    {
        'name': 'Home',
        'templates': ['homepage.html'],
        'link': '/'
    },
    {
        'name': 'About',
        'templates': ['about.html'],
        'link': '/'
    },
    {
        'name': 'Blog',
        'templates': ['blog_feed.html', 'blog_post.html'],
        'link': '/blog/'
    },
    {
        'name': 'Contact',
        'templates': ['contact.html'],
        'link': '/contact/'
    },
]

class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = [m for m in PAGES if self.template_name not in m['templates']]
        return context
