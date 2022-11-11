from django.db import models
class TextSum(models.Model):
    text=models.CharField(max_length=200, blank=True,null=True)
    data=models.TextField(blank=True,null=True)
    summary=models.CharField(max_length=1000,blank=True,null=True)
class PythonSum(models.Model):
    code=models.TextField(blank=True,null=True)
    summary=models.CharField(max_length=500,blank=True,null=True)
class TextImgSum(models.Model):
    name=models.CharField(max_length=200, blank=True,null=True)
    img=models.ImageField(upload_to='summariser/files/imgs')
    # summary=models.CharField(max_length=1000,blank=True,null=True)
