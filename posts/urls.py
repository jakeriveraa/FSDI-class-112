from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,  
    PostUpdateView,
    PostDeleteView,
    DraftPostListView,
    ArchivedPostListView
)


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("detailed/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("archived/", ArchivedPostListView.as_view(), name="post_archive"),
    path('drafts/', DraftPostListView.as_view(), name='draft_post')
]