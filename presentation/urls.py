
from django.urls import path
from .views import home, search_article, view_article, tag_search


urlpatterns = [
    path('', home, name='home'),
    path('search/', search_article, name='search_article'),
    path('detail/', view_article, name='view_article'),
    path('tags/', tag_search, name='tag_search')
]