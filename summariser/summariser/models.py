from django.db import models
class TextSum(models.Model):
    text=models.CharField(max_length=200, blank=True,null=True)
    summary=models.CharField(max_length=500, blank=True,null=True)