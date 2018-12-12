from django.shortcuts import render, redirect
from .models import Article
from django.utils import timezone

# Create your views here.
def home(request):
    list_articles = list(Article.objects.all())
    return render(request, 'authoring/home.html', {'articles': list_articles})

def new_article(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['header'] and request.POST['fulltext']:
            article = Article()
            article.title = request.POST['title']
            article.content = request.POST['fulltext']
            article.header = request.FILES['header']
            article.pub_date = timezone.datetime.now()
            article.save()
            return redirect('home')
        else:
            return render(request, 'authoring/new.html', {'error': 'All Fields Required'})
    else:
        return render(request, 'authoring/new.html')

def view_article(request):
    article_id = request.GET['id']
    if article_id:
        article = Article.objects.get(id=article_id)
        return render(request, 'authoring/detail.html', {'article' : article})
    else:
        return redirect('home')

def edit_article(request):
    if request.method == 'POST':
        article = Article.objects.get(title=request.POST['title'])
        if request.POST['fulltext']:
            article.content = request.POST['fulltext']
            article.save()
            return redirect('home')
        else:
            return render(request, 'authoring/edit.html', {'article': article})
    else:
        article_id = request.GET['id']
        if article_id:
            article = Article.objects.get(id=article_id)
            return render(request, 'authoring/edit.html', {'article': article})
        else:
            return redirect('home')
        