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
            data = dict(message="Please register to continue...")
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        if request.user.is_authenticated:
            data = request.data
            serializer = PostSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(author=request.user)
        else:
            data = dict(message="Unauthenticated user or rule violation")
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request: Request, *args, **kwargs):
        if request.user.is_anonymous:
            data = dict(message="Please register to continue...")
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        instance = Post.objects.get(id=kwargs["pk"])
        if request.user.is_authenticated and request.user == instance.author:
            data = request.data
            serializer = PostSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            data = dict(message="Unauthenticated user or rule violation")
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            data = dict(message="Please register to continue...")
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        instance = Post.objects.get(id=kwargs["pk"])
        if request.user.is_authenticated and request.user == instance.author:
            instance.delete()
        else:
            data = dict(message="Unauthenticated user or rule violation")
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        return Response(status=status.HTTP_204_NO_CONTENT)
