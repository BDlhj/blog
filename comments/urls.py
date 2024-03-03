from django.urls import path
from comments.views import CommentListView, CommentDetailView


urlpatterns = [
    path("posts/<int:post_id>/", CommentListView.as_view()),
    path("<int:pk>/", CommentDetailView.as_view()),
]
