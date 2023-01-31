from rest_framework import viewsets
from core.models import tourist_places  
from .serializers import TouristPlacesSerializer

class TouristPlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = tourist_places.objects.all()
    serializer_class = TouristPlacesSerializer