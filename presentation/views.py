from django.shortcuts import render, redirect
from authoring.models import Article
import requests
# Create your views here.
def home(request):
    featurestory = Article.objects.latest()
    articles = Article.objects.all()
    return render(request, 'presentation/index.html', 
    { 'featurestory' : featurestory, 'articles': articles})

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