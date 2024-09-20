from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:50]


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project_direction = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    client = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    images = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Block(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    descriptions = models.TextField()
    images = models.ImageField(upload_to='images2/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
