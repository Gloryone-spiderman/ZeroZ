from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = "__all__"
        # fields = ("id", "content", "created_at")
        fields = ['id', 'content', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comment = CommentSerializer(many=True, read_only=True)
    # article.comments.all()
    class Meta:
        model = Article
        # fields = "__all__"
        # fields = ("id", "title", "content", "created_at")
        fields = ['id', 'title', 'content','author', 'created_at', 'comment']
