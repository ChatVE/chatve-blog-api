from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    pass


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'date_posted',
            'body',
        ]