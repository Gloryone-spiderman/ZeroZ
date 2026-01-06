from django.contrib import admin
from .models import Article,Comment
# 让管理员可以管理文章
admin.site.register(Article)
admin.site.register(Comment)
# Register your models here.
