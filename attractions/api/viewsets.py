from rest_framework import viewsets
from attractions.models import attraction
from .serializers import AttractionSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AttractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']