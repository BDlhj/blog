from rest_framework import serializers
from posts.models import Post
from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["content"]
