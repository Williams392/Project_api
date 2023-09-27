from django.contrib import admin
from .models import Post, Image, Video, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('member', 'content', 'timestamp')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'timestamp')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('post', 'video', 'timestamp')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'timestamp')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
