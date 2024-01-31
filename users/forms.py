from django.contrib.auth.forms import UserCreationForm
from users.models import User ,User_profile
from django import forms

        

class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'first_name'  ,  'last_name' , 'email' , 'password1'  ,  'password2']
   


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ['bio', 'city', 'phone', 'image']