from django.db import models
from django.contrib.auth.models import User, AbstractUser 
from django.utils import timezone


class User(AbstractUser):
    pass

class User_profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000, default="lahore")
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField( default='default.jpg',null= True, upload_to='profile_pic' )
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}'
