from django.urls import path
from posts.views import PostListView, PostDetailView


urlpatterns = [
    path("", PostListView.as_view()),
    path("<int:pk>/", PostDetailView.as_view()),
]
