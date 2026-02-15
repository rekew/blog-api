from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)
from .models import Post, Comment


class PostSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('author', "inserted_at", "updated_at")


class CommentSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('author', "inserted_at", "updated_at")
