from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Post
from posts.serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer
from posts.permissions import IsAdminUserOrAuthorOrReadOnly
from tags.models import Tag


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

    def perform_destroy(self, instance):
        tags = instance.tags.all()
        
        for tag in tags:
            if tag.posts.count() + tag.comments.count() == 1:
                tag.delete()

        instance.delete()
