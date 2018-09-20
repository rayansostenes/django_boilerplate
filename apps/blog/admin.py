from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'body']
    prepopulated_fields = {'slug': ('title',),}

# Register your models here.
