from django.db import models

class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
