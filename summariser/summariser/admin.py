from django.contrib import admin
from .models import TextSum,PythonSum
class TextSumAdmin(admin.ModelAdmin):
      TextSum    = ['text', 'data', 'summary']
class PySumAdmin(admin.ModelAdmin):
    list1=['code','summary']
admin.site.register(PythonSum,PySumAdmin)
admin.site.register(TextSum, TextSumAdmin)