from django.db import models
from datetime import date

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    date = models.DateField(default=date.today())
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title