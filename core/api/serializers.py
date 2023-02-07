from rest_framework.serializers import ModelSerializer
from core.models import tourist_places
from attractions.api.serializers import AttractionSerializer
from localization.api.serializers import LocalizationSerializer


class TouristPlacesSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    address = LocalizationSerializer()


    class Meta:
        model = tourist_places
        fields = ('id', 'name','description','approved','attractions',
                  'comments','assessments','address','picture')
      