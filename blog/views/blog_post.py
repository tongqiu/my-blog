from django.http import HttpResponse
from django.views.generic import TemplateView

from blog.models import BlogPost

class BlogPostView(TemplateView):
    template_name = 'blog_post.html'
    blogpost = None

    def get(self, request, slug):
        blogposts = BlogPost.objects.filter(slug=slug)
        if blogposts.exists():
            self.blogpost = blogposts[0]
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.blogpost:
            context.update({
                'title': self.blogpost.title,
                'content': self.blogpost.content,
                'publish_date': self.blogpost.created_datetime.strftime('%d %B %Y')
            })
        return context
