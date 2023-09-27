from django.db import models
from clubs.models import Member

# Create your models here.
class Post(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Otros campos relevantes para las publicaciones

class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    timestamp = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    post = models.ForeignKey(Post, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='post_videos/')
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Otros campos relevantes para los comentarios

class Like(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    # Otros campos relevantes para los me gusta