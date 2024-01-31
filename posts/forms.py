from django import forms
from .models import PostModel , Comment, Reply


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'description', 'post_image', 'privacy']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']