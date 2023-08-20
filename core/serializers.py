from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'name',
            'post',
            'comment',
            'date_posted',
        ]


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'date_posted',
            'body',
            'comment',
        ]