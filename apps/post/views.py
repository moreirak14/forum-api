from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.post.models import Post
from apps.post.serializers import PostSerializer


class PostViewSets(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request: Request, *args, **kwargs):
        if request.user.is_anonymous:
            return

        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
