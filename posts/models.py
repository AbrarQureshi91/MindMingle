from django.db import models
from users.models import User
from django.utils import timezone


class PostModel(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    post_image = models.ImageField(upload_to='posts_image' , null= True , blank=True)
    create_time = models.DateTimeField(default = timezone.now)
    privacy = models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    def user_has_liked(self, user):
        return self.likes.filter(user=user).exists()
    
class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class SharedPost(models.Model):
    original_post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_posts')
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_posts')
    created_at = models.DateTimeField(default=timezone.now)