from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=400)
    date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.text