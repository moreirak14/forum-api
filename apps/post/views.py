from rest_framework.viewsets import ModelViewSet

from apps.post.models import Post
from apps.post.serializers import PostSerializer


class PostViewSets(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
