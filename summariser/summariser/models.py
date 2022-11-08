from django.db import models
class TextSum(models.Model):
    text=models.CharField(max_length=200, blank=True,null=True)
    data=models.TextField(blank=True,null=True)
    summary=models.CharField(max_length=1000,blank=True,null=True)
