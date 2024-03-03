from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from comments.models import Comment
from comments.serializers import CommentSerializer
from posts.models import Post
from posts.permissions import IsAdminUserOrAuthorOrReadOnly


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.method == "GET":
            post_id = self.kwargs.get("post_id")
            post = get_object_or_404(Post, pk=post_id)
            return Comment.objects.filter(post=post)
        return Comment.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=author, post=post)


class CommentDetailView(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUserOrAuthorOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(is_updated=True)
