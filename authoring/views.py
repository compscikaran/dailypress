from django.shortcuts import render, redirect
from .models import Article
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    list_articles = Article.objects.filter(author=request.user)
    return render(request, 'authoring/home.html', {'articles': list_articles})

@login_required
def new_article(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['header'] and request.POST['fulltext']:
            article = Article()
            article.title = request.POST['title']
            article.content = request.POST['fulltext']
            article.header = request.FILES['header']
            article.tags = request.POST['tags'] if 'tags' in request.POST.keys() else None 
            article.pub_date = timezone.datetime.now()
            article.author = request.user
            article.save()
            return redirect('all_articles')
        else:
            return render(request, 'authoring/new.html', {'error': 'All Fields Required'})
    else:
        return render(request, 'authoring/new.html')

@login_required
def view_article(request):
    article_id = request.GET['id']
    if article_id:
        article = Article.objects.get(id=article_id)
        return render(request, 'authoring/detail.html', {'article' : article})
    else:
        return redirect('home')

@login_required
def edit_article(request):
    if request.method == 'POST':
        article = Article.objects.get(title=request.POST['title'])
        if request.POST['fulltext']:
            article.content = request.POST['fulltext']
            article.save()
            return redirect('all_articles')
        else:
            return render(request, 'authoring/edit.html', {'article': article})
    else:
        article_id = request.GET['id']
        if article_id:
            article = Article.objects.get(id=article_id)
            return render(request, 'authoring/edit.html', {'article': article})
        else:
            return redirect('home')
        