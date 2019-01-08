from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    # In Django2.0, CASCADE is not a default value for on_delete
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE,)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())

    class Meta:
        # desc
        ordering = ("-publish",)

    def __str__(self):
        return self.title
