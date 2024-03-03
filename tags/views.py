from rest_framework import generics
from tags.models import Tag
from tags.serializers import TagPostSerializer, TagCommentSerializer


class PostsByTagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagPostSerializer


class CommentsByTagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCommentSerializer

