from rest_framework import viewsets
from comments.models import comment 
from .serializers import CommentsSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = comment.objects.all()
    serializer_class = CommentsSerializer