from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter,SearchFilter
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    ordering_fields = ['title','created_at']


class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetailAPIView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class ArticleCreateAPIView(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class ArticleUpdateAPIView(APIView):
    def put(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class ArticleDeleteAPIView(APIView):
    def delete(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status=204)
