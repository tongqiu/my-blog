from django.db import models
from django.db.models import permalink

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    created_datetime = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    @permalink
    def get_absolute_url(self):
        return ('view-blog-post', [self.slug])
