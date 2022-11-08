from django.contrib import admin
from .models import TextSum
class TextSumAdmin(admin.ModelAdmin):
      TextSum    = ['text', 'data', 'summary']
admin.site.register(TextSum, TextSumAdmin)