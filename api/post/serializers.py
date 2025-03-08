from rest_framework import serializers
from content.models import Post

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",
            "uuid",
            "title",
            "body",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "uuid",
            "owner",
            "created_at",
        ]
