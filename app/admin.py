from django.contrib import admin
from .models import book

# Register your models here.

class bookadmin(admin.ModelAdmin):
    list_display=('name' , 'author' , 'price')

admin.site.register(book , bookadmin)    