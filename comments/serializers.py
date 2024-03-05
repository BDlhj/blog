from rest_framework import serializers
from comments.models import Comment
from tags.models import Tag
from tags.serializers import TagSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        tags_list = validated_data.pop("tags", [])
        tags_list = [tag.replace(' ', '') for tag in tags_list]
        comment = Comment.objects.create(**validated_data)
        
        for tag in tags_list:
            tag, created = Tag.objects.get_or_create(content=tag)

        comment.tags.set(tags_list)
        
        return comment
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        tags = instance.tags.all()
        res.update({'tags': [TagSerializer(tag).data["content"] for tag in tags]})
        return res
