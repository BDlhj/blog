from rest_framework import serializers
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    truncated_description = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        exclude = ["description"]


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
