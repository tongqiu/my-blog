from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse

from blog.models import BlogPost

class BlogFeedView(TemplateView):
    template_name = 'blog_feed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_posts = BlogPost.objects.all().order_by('-created_datetime')
        blog_feed = []
        for post in blog_posts:
            words = post.content.split(' ')
            excerpt = ' '.join(words[:60])
            if excerpt.endswith('.'):
                excerpt = excerpt[:-1]
            blog_feed.append({
                'title': post.title,
                'date': post.created_datetime.strftime('%d %B %Y'),
                'text': excerpt,
                'link': reverse("blog-post", kwargs={'slug': post.slug})
            })
        context['blog_feed'] = blog_feed
        return context
