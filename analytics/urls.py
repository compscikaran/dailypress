
from django.urls import path
from .views import counter, hits


urlpatterns = [
    path('counter/', counter, name='counter'),
    path('', hits, name='hits'),
]