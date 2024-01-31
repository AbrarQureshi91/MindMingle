from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from posts.models import User , Comment , Like , SharedPost ,PostModel
from .forms import PostForm , CommentForm, ReplyForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin  ,  CreateView):
    login_url = '/login/'
    model = PostModel
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostListView( ListView):
    
    model = PostModel
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDeleteView( LoginRequiredMixin , DeleteView):
    login_url = '/login/'
    model = PostModel
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list')


class PostDetailView( LoginRequiredMixin , View):
    login_url = '/login/'
    template_name = 'post_detail.html'

    def get(self, request, pk):
        post = get_object_or_404(PostModel, pk=pk)
        comment_form = CommentForm()
        reply_form = ReplyForm()
        return render(request, self.template_name, {'post': post, 'comment_form': comment_form, 'reply_form': reply_form})

    def post(self, request, pk):
        post = get_object_or_404(PostModel, pk=pk)
        comment_form = CommentForm(request.POST)
        reply_form = ReplyForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.comment = get_object_or_404(Comment, pk=request.POST.get('comment_id'))
            reply.user = request.user
            reply.save()

        if 'like' in request.POST:
            liked = Like.objects.filter(post=post, user=request.user)
            if liked.exists():
                liked.delete()
            else:
                Like.objects.create(post=post, user=request.user)

        if 'share' in request.POST:
            shared_with_username = request.POST.get('share_with_username')
            shared_with_user = User.objects.get(username=shared_with_username)
            
            if not SharedPost.objects.filter(original_post=post, shared_by=request.user, shared_with=shared_with_user).exists():
                SharedPost.objects.create(original_post=post, shared_by=request.user, shared_with=shared_with_user)

        return redirect('post_detail', pk=pk)

@login_required
def user_page(request , username):

    user = get_object_or_404(User , username=username)
    posts = PostModel.objects.filter(user=user)
    return render(request , 'user_page.html' , { 'user': user , 'posts': posts})  
