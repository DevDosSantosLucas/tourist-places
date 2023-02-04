from rest_framework import viewsets
from localization.models import  localization
from .serializers import LocalizationSerializer

class LocalizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = localization.objects.all()
    serializer_class = LocalizationSerializer