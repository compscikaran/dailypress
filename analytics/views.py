from django.shortcuts import render
from .models import ArticleHit
from authoring.models import Article
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Count
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

def hits(request):
    list_hits = list(ArticleHit.objects.all().values('article').annotate(total=Count('article')).order_by('article'))
    list_articles = list(Article.objects.all())
    for i in range(0, len(list_hits)):
        list_hits[i]['title'] = list_articles[i].title
    return render(request, 'analytics/hits.html', {'list_hits' : list_hits})
