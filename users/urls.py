from django.urls import path
from users import views
from .views import UserProfileCreateView, UserProfileUpdateView, UserProfileDetailView, UserProfileDeleteView, UserProfileListView



urlpatterns = [
      path('signup/' , views.Signup , name= 'Signup'),
    path('login/' , views.loginpage , name = 'loginpage'),
    path('' , views.Homepage , name='Homepage'),
     path('profile/create/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/update/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', UserProfileDeleteView.as_view(), name='profile-delete'),
    path('profile/', UserProfileListView.as_view(), name='profile-list'),
     path('logout/', views.logout_profile, name='logout')
]



