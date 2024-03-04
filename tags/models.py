from django.db import models
from posts.models import Post
from comments.models import Comment


class Tag(models.Model):
    content = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class TagPostSet(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class TagCommentSet(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

