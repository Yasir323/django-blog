from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


def current_time():
    return timezone.localtime(timezone.now())


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=current_time)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.IntegerField()
    # share = models.BooleanField()

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
