from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    header = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()