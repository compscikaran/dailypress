from django.db import models
from authoring.models import Article
# Create your models here.

class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
