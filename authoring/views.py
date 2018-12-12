from django.shortcuts import render, redirect
from .models import Article
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'authoring/home.html')

def new(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['header'] and request.POST['content']:
            article = Article()
            article.title = request.POST['title']
            article.content = request.POST['content']
            article.header = request.FILES['header']
            article.pub_date = timezone.datetime.now()
            article.save()
            return redirect('home')
        else:
            return render(request, 'authoring/editor.html', {'error': 'All Fields Required'})
    else:
        return render(request, 'authoring/editor.html')
    