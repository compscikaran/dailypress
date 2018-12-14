
from django.urls import path
from .views import home, new_article, view_article, edit_article


urlpatterns = [
    path('all/', home, name='all_articles'),
    path('new/', new_article, name='new_article'),
    path('view/', view_article, name='preview_article'),
    path('edit/', edit_article, name='edit_article')
]