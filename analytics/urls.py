
from django.urls import path
from .views import counter, hits, visit_data, graph


urlpatterns = [
    path('counter/', counter, name='counter'),
    path('', hits, name='hits'),
    path('hits/', visit_data, name='visit_data'),
    path('graph/', graph, name='graph'),
]