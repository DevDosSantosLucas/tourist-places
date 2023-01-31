from rest_framework.serializers import ModelSerializer
from core.models import tourist_places 

class TouristPlacesSerializer(ModelSerializer):
    class Meta:
        model = tourist_places
        fields = ('id', 'name','description')#,'approved','attractions','comments','assessments','address')
      