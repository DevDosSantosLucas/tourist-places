from rest_framework.serializers import ModelSerializer
from assessments.models import assessment

class AssessmentSerializer(ModelSerializer):
    class Meta:
        model = assessment
        fields = ('id','user','comment', 'note','date')

