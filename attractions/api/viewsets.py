from rest_framework import viewsets
from attractions.models import attraction
from .serializers import AttractionSerializer

class AttractionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = attraction.objects.all()
    serializer_class = AttractionSerializer