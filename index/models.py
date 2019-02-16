from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)
        verbose_name = '垃圾博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title