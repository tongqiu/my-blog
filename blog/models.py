from django.db import models
from django.urls import reverse

class Quote(models.Model):
    author = models.CharField(max_length=120)
    text = models.TextField()
    created_datetime = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '{}_{}'.format(self.author, self.id)

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    created_datetime = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
