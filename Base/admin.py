from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


# @admin.register(models.Post)

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'status', 'excerpt', 'author','BookCoverImage','published','ClosingTime')
    

admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.Response)
admin.site.register(models.Question)
admin.site.register(models.SubscribedPosts)

