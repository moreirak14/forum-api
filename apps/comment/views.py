from rest_framework.viewsets import ModelViewSet

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer


class CommentViewSets(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
