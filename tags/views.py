from rest_framework import generics
from tags.models import Tag
from tags.serializers import TagPostSerializer, TagCommentSerializer
from django.shortcuts import get_object_or_404

class PostsByTagListView(generics.ListAPIView):
    serializer_class = TagPostSerializer

    def get_queryset(self):
        content = self.kwargs["pk"]
        tag = get_object_or_404(Tag, content=content)
        return tag.posts.all()


class CommentsByTagListView(generics.ListAPIView):
    serializer_class = TagCommentSerializer

    def get_queryset(self):
        content = self.kwargs["pk"]
        tag = get_object_or_404(Tag, content=content)
        return tag.comments.all()
