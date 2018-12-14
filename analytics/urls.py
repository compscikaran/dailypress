
from django.urls import path
from .views import counter


urlpatterns = [
    path('counter/', counter, name='counter'),
]