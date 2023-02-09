from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from attractions.models import attraction as Attraction
from localization.models import localization as Localization

from core.models import tourist_places
from attractions.api.serializers import AttractionSerializer
from localization.api.serializers import LocalizationSerializer

class TouristPlacesSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True )#, read_only=True)
    address = LocalizationSerializer()#read_only=True)
    full_description = SerializerMethodField()


    class Meta:
        model = tourist_places
        fields = ('id', 'name','description','approved','attractions',
                  'comments','assessments','address','picture',
                  'full_description','full_description2')
        
        read_only_fields = ('comments','assessments')

    def create_attractions(self, attractions, place):
        for attraction in attractions:
            at = Attraction.objects.create(**attraction)
            place.attractions.add(at)
    
    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']

        address = validated_data['address']
        del validated_data['address']

        place = tourist_places.objects.create(**validated_data)
        self.create_attractions(attractions, place)

        local = Localization.objects.create(**address)
        place.address = local 
        place.save() 

        return place
         
    def get_full_description(self, object):
        return '%s - %s' % (object.name,object.description)