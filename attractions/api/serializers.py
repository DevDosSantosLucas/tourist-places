from rest_framework.serializers import ModelSerializer
from attractions.models import attraction

class AttractionSerializer(ModelSerializer):
    class Meta:
        model = attraction
        fields = ('id','name','description','opening_hours', 'minimum_age','picture')

