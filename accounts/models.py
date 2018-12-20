from django.db import models

# Create your models here.
class AuthorizationKey(models.Model):
    key = models.CharField(max_length=255)

