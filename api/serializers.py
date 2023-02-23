from rest_framework import serializers
from django.contrib.auth.models import User
from blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Blog
        fields = ['id', 'blog_title', 'content', 'created_by', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'blogs']