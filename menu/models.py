from django.db import models


# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
