from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Tada(models.Model):
    tada_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.tada_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Module(models.Model):
    tada = models.ForeignKey(Tada, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=200)
    module_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.module_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)