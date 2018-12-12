
from django.urls import path
from .views import *

urlpatterns = [
    path('new/', new, name='new_article')
]