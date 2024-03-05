from django.shortcuts import get_object_or_404
from rest_framework import generics
from comments.serializers import CommentSerializer
from posts.serializers import PostListSerializer
from tags.models import Tag


class PostsByTagListView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        content = self.kwargs["pk"]
        tag = get_object_or_404(Tag, content=content)
        return tag.posts.all()


class CommentsByTagListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        content = self.kwargs["pk"]
        tag = get_object_or_404(Tag, content=content)
        return tag.comments.all()
