from django.contrib import admin
from .models import *

# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    list_display = ['title','search' ,'created']



admin.site.register(Search ,SearchAdmin)
