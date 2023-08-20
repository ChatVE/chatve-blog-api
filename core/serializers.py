from rest_framework import serializers
from django.contrib.auth.models import User
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    author = UserSerializer()
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'date_posted',
            'body',
            'comment',
        ]