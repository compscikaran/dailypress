from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    header = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.TextField(null=True)

    class Meta:
        get_latest_by = 'pub_date'