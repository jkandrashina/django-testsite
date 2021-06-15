from django.conf import settings
from django.db import models
import datetime

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=datetime.date.today)
    tags = models.CharField(max_length=400)

    def __str__(self):
        return self.title

    def tags_as_list(self):
        return [i.strip() for i in self.tags.split(',')]
