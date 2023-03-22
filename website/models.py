from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_created=True, auto_now_add=True, blank=True)

    def __str__(self):
        return "Title:\t" + self.title
