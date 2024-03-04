from django.urls import path
from tags.views import PostsByTagListView, CommentsByTagListView


urlpatterns = [
    path("<str:pk>/posts/", PostsByTagListView.as_view()),
    path("<str:pk>/comments/", CommentsByTagListView.as_view()),
]
