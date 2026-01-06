from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='articles')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
