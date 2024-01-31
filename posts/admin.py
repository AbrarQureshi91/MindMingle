from django.contrib import admin
from posts.models import PostModel , Comment , Reply , SharedPost , Like
# Register your models here.



admin.site.register(PostModel)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(SharedPost)
admin.site.register(Like)
