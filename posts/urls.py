from django.urls import path
from .views import PostCreateView, PostListView, PostDeleteView ,PostDetailView
from posts import views
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('list/', PostListView.as_view(), name='post_list'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

]
