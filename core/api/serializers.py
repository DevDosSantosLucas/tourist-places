from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import tourist_places
from attractions.api.serializers import AttractionSerializer
from localization.api.serializers import LocalizationSerializer

class TouristPlacesSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    address = LocalizationSerializer()
    full_description = SerializerMethodField()


    class Meta:
        model = tourist_places
        fields = ('id', 'name','description','approved','attractions',
                  'comments','assessments','address','picture',
                  'full_description','full_description2')
      
    
    def get_full_description(self, object):
        return '%s - %s' % (object.name,object.description)