from rest_framework.serializers import ModelSerializer
from comments.models import comment

class CommentsSerializer(ModelSerializer):
    class Meta:
        model = comment
        fields = ('id','user','comment','date','approved')
        