from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'title', 'rating')
    list_filter = ['dateCreation']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
