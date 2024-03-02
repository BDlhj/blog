from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostListSerializer, PostCreateSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostListSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)

