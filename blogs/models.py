from django.db import models

from pages.models import BaseModel


class BlogModel(BaseModel):
    author = models.CharField(max_length=50, default='Admin')
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    video = models.FileField(upload_to='blog_videos/', blank=True, null=True)

    def __str__(self):
        return self.title
