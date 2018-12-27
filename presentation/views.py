from django.shortcuts import render, redirect
from authoring.models import Article
import requests
# Create your views here.
def home(request):
    featurestory1 = Article.objects.latest()
    featurestory2 = Article.objects.all().order_by('-pub_date')[1]
    articles = Article.objects.all().order_by('-pub_date')[2:]
    if featurestory1 is None:
        return render(request, 'presentation/index.html')
    elif featurestory2 is None:
        return render(request, 'presentation/index.html', 
        { 'featurestory1': featurestory1 })
    elif articles is None:
        return render(request, 'presentation/index.html', 
        { 'featurestory1': featurestory1, 'featurestory2': featurestory2 })
    return render(request, 'presentation/index.html', 
    { 'featurestory1' : featurestory1, 'featurestory2': featurestory2, 'articles': articles})

def search_article(request):
    if request.method == 'GET':
        if request.GET['query']:
            query = request.GET['query']
            articles = Article.objects.filter(title__icontains=query)
            return render(request, 'presentation/search.html', 
            {'query' : query, 'articles': articles})
        else:
            return redirect('home')
    else:
        return redirect('home')

def view_article(request):
    if request.method == 'GET':
        if request.GET['id']:
            article_id = request.GET['id']
            article = Article.objects.get(id=article_id)
            tags = article.tags.split(',') if article.tags is not None else []
            requests.get('http://' + request.get_host() + '/analytics/counter/?id=' + str(article_id))
            return render(request, 'presentation/detail.html', { 'article': article, 'tags': tags})
        else:
            return redirect('home')
    else:
        return redirect('home')

def tag_search(request):
    if request.method == 'GET':
        if request.GET['tag']:
            tag = request.GET['tag']
            articles = Article.objects.filter(tags__icontains=tag)
            return render(request, 'presentation/search.html', 
            {'query' : tag, 'articles': articles})
        else:
            return redirect('home')
    else:
        return redirect('home')