import markdown

from django.http import HttpResponse
from django.urls import reverse

from blog.models import BlogPost
from blog.views.base import BaseView

class BlogPostView(BaseView):
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
            try:
                previous_post = self.blogpost.get_previous_by_created_datetime()
            except BlogPost.DoesNotExist:
                previous_post = None
            try:
                next_post = self.blogpost.get_next_by_created_datetime()
            except BlogPost.DoesNotExist:
                next_post = None

            context.update({
                'title': self.blogpost.title,
                'content': markdown.markdown(self.blogpost.content,
                                             extensions=['markdown.extensions.nl2br']),
                'publish_date': self.blogpost.created_datetime.strftime('%d %B %Y')
            })

            if previous_post:
                context.update({
                    'previous_post_link': reverse("blog-post", kwargs={'slug': previous_post.slug}),
                    'previous_post_title': previous_post.title
                })

            if next_post:
                context.update({
                    'next_post_link': reverse("blog-post", kwargs={'slug': next_post.slug}),
                    'next_post_title': next_post.title
                })
        return context
