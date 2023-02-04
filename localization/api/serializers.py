from rest_framework.serializers import ModelSerializer
from localization.models import localization 

class LocalizationSerializer(ModelSerializer):
    class Meta:
        model = localization
        fields = ( 'line1','line2','city','state','country','latitude','longitude')
      