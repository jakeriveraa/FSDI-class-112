from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = "posts"
    
    def get_queryset(self):
        published_status = Status.objects.get(name="published")
        return Post.objects.filter(status=published_status)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"    
    model = Post
    context_object_name = "single_post"


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title","subtitle","body","status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/update.html"
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']

    def test_func(self):
        post = self.get_object() # -> posts/detail/2/ (test1) post obj(title, subtitle, author, status)
        if self.request.user.is_authenticated: #True
            return self.request.user == post.author # admin == testUser1 (false)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy('post_list')


class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/drafts.html"
    model = Post
    context_object_name = "draft_posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["draft_posts"] = (
            Post.objects
            .filter(status=draft_status, author=self.request.user)
            .order_by("-created_on")
        )
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/archived.html"
    archived_status = Status.objects.get(name="draft")
    queryset = Post.objects.filter(status=archived_status).order_by("created_on").reverse()

    context_object_name = "archived_posts"