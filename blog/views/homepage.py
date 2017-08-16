from django.http import HttpResponse
from django.views.generic import TemplateView

from blog.models import Quote

class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quote = Quote.objects.all().order_by('-created_datetime').first()
        context.update({
            'author': quote.author,
            'text': quote.text
        })
        return context
