from rest_framework import viewsets
from assessments.models import assessment
from .serializers import AssessmentSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = assessment.objects.all()
    serializer_class = AssessmentSerializer
