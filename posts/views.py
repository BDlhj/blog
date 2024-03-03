from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Post
from posts.serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer
from posts.permissions import IsAdminUserOrAuthorOrReadOnly


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostListSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAdminUserOrAuthorOrReadOnly]
