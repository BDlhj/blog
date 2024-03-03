from rest_framework import serializers
from posts.models import Post
from tags.serializers import TagSerializer
from tags.models import Tag


class PostListSerializer(serializers.ModelSerializer):
    truncated_description = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        exclude = ["description", "tags"]


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        tags_list = validated_data.pop("tags", [])
        post = Post.objects.create(**validated_data)

        for tag in tags_list:
            tag, created = Tag.objects.get_or_create(content=tag)

        post.tags.set(tags_list)

        return post
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        tags = instance.tags.all()
        res.update({'tags': [TagSerializer(tag).data["content"] for tag in tags]})
        return res


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"
