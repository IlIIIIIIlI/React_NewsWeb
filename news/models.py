from django.db import models

# Create your models here.


class NewsDetail(models.Model):
    newsdetail=models.JSONField()