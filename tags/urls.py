from django.urls import path
from tags.views import PostsByTagListView, CommentsByTagListView


urlpatterns = [
    path("<int:pk>/posts/", PostsByTagListView.as_view()),
    path("<int:pk>/comments/", CommentsByTagListView.as_view()),
]
