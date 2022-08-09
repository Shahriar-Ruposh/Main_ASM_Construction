from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Author, Category, Post, Comment, PostView
from django.db import models
# Register your models here.
class textEditorAdmin(admin.ModelAdmin):
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }

admin.site.register(Post,textEditorAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(PostView)