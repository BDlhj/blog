from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["content"]


class TagPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
