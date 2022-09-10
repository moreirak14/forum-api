from rest_framework import serializers

from apps.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")

    class Meta:
        model = Post
        fields = ["id", "title", "description", "author"]
