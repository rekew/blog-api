<<<<<<< HEAD
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, CommentSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

import logging

logger = logging.getLogger('blogs')

class PostViewSet(ModelViewSet):

    lookup_field = "slug"

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(status="published")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthorOrReadOnly()]
        return super().get_permissions()

    @action(detail=True, methods=['get', 'post'], url_path='comments')
    def comments(self, request, slug=None):
        post = self.get_object()

        if request.method == "GET":
            comments = post.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, post=post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 006ac0f38acdf1843bb88b1b22489f0a4a6405c8
