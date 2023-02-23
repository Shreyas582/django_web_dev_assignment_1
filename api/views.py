from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from api import serializers
from django.contrib.auth.models import User
from blogs.models import Blog
from api.permissions import IsOwnerOrReadOnly

@permission_classes([IsAdminUser])
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

@permission_classes([IsAdminUser])
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

@permission_classes([IsAdminUser])
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

@permission_classes([IsAdminUser])
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]