from rest_framework import serializers
from content.models import Post
from api.user.serializers import UserPublicSerializer
#from django.contrib.auth import get_user_model

#User = get_user_model()

class PostSerializers(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "uuid",
            "title",
            "owner",
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
