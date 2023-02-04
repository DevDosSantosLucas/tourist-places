from rest_framework.response import Response
from rest_framework import viewsets
from core.models import tourist_places  
from .serializers import TouristPlacesSerializer

class TouristPlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = tourist_places.objects.all()
    serializer_class = TouristPlacesSerializer

    def get_queryset(self):
       return tourist_places.objects.filter(approved=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})
    
    def create(self, request, *args, **kwargs):
        return Response({'return': request.data['name']})