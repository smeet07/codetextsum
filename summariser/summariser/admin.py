from django.contrib import admin
from .models import TextSum,PythonSum,TextImgSum
class TextSumAdmin(admin.ModelAdmin):
      TextSum    = ['text', 'data', 'summary']
class PySumAdmin(admin.ModelAdmin):
    list1=['code','summary']

class TextImgSumAdmin(admin.ModelAdmin):
    list1=['name','img']

admin.site.register(PythonSum,PySumAdmin)
admin.site.register(TextSum, TextSumAdmin)
admin.site.register(TextImgSum,TextImgSumAdmin)