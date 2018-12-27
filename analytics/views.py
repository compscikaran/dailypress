from django.shortcuts import render
from .models import ArticleHit
from authoring.models import Article
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def counter(request):
    article_id = request.GET['id']
    article = Article.objects.get(id=article_id)
    article_hit = ArticleHit()
    article_hit.article = article
    article_hit.timestamp = timezone.now()
    article_hit.save()
    response = 'Article ' + str(article.id) + ' Counted'
    return JsonResponse({'msg' : response})

@login_required
def hits(request):
    list_hits = list(ArticleHit.objects.all().values('article').annotate(total=Count('article')).order_by('article'))
    list_articles = list(Article.objects.all())
    for i in range(0, len(list_hits)):
        list_hits[i]['title'] = list_articles[i].title
    return render(request, 'analytics/hits.html', {'list_hits' : list_hits})

@login_required
def visit_data(request):
    article_id = request.GET["id"]
    article = Article.objects.get(id=article_id)
    list_hits = list(ArticleHit.objects.filter(article = article).values('timestamp'))
    dates = [str(item['timestamp'].date()) for item in list_hits]
    response = {}
    for date in dates:
        if date in response.keys():
            response[date] += 1
        else:
            response[date] = 1
    return_value = {}
    return_value['labels'] = list(response.keys())
    return_value['values'] = list(response.values())
    return JsonResponse(return_value, safe=False)

@login_required
def graph(request):
    article_id = request.GET["id"]
    return render(request, 'analytics/visits.html', {'id': article_id})