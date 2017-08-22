from django.http import HttpResponse
from django.urls import reverse

from django.views.generic import TemplateView


PAGES = [
    {
        'name': 'Home',
        'template': 'homepage.html',
        'link': '/'
    },
    {
        'name': 'About',
        'template': 'about.html',
        'link': '/'
    },
    {
        'name': 'Blog',
        'template': 'blog_feed.html',
        'link': '/blog/'
    },
    {
        'name': 'Contact',
        'template': 'contact.html',
        'link': '/contact/'
    },
]

class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = [m for m in PAGES if m['template'] != self.template_name]
        return context
