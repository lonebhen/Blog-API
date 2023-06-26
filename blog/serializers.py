from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.author')

    class Meta:
        model = Post
        fields = ["id", "author", "title",
                  "content", "created_at", "updated_at"]
