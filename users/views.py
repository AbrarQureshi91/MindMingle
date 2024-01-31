from django.shortcuts import render , redirect , HttpResponse
from django.urls import reverse_lazy
from  users.forms import Signup_form , UserProfileForm
from django.contrib.auth import authenticate,login, logout
from .models import User ,  User_profile
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin




def Signup(request):
    if request.method == 'POST' :
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
        else:
           return HttpResponse(form.error_messages)
    else:
        form = Signup_form()

    return render(request , 'signup.html' , {'form' : form} )



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('Homepage')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
         
    return render(request, 'login.html')



class UserProfileCreateView( LoginRequiredMixin , CreateView):
    login_url = '/login/'
    model = User_profile
    form_class = UserProfileForm
    template_name = 'user_profile_create.html'
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserProfileUpdateView( LoginRequiredMixin , UpdateView):
    login_url = '/login/'
    model = User_profile
    form_class = UserProfileForm
    template_name = 'user_profile_update.html'
    success_url = '/profile/'

class UserProfileDetailView(LoginRequiredMixin ,  DetailView):
    login_url = '/login/'
    model = User_profile
    template_name = 'user_profile_detail.html'

class UserProfileDeleteView( LoginRequiredMixin ,  DeleteView):
    login_url = '/login/'
    model = User_profile
    template_name = 'user_profile_delete.html'
    success_url = '/profile/'

class UserProfileListView(LoginRequiredMixin ,  ListView):
    login_url = '/login/'
    model = User_profile
    template_name = 'user_profile_list.html'
    context_object_name = 'profiles'



def Homepage(request):

  return render(request , 'home.html')

def logout_profile(request):

    logout(request)
    return redirect('Homepage')