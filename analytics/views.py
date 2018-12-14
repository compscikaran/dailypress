from django.shortcuts import render
from .models import ArticleHit
from authoring.models import Article
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.

def counter(request):
    article_id = request.GET['id']
    article = Article.objects.get(id=article_id)
    article_hit = ArticleHit()
    article_hit.article = article
    article_hit.timestamp = timezone.now()
    article_hit.save()
    response = 'Article ' + str(article.id) + ' Counted'
    return JsonResponse({'msg' : response})