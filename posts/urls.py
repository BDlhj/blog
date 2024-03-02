from django.urls import path
from posts.views import PostListView


urlpatterns = [
    path("", PostListView.as_view()),
]
