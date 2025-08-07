from django.db import models

from pages.models import BaseModel


class BlogModel(BaseModel):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
       return self.title

