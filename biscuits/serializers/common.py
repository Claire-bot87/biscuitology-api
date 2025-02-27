from rest_framework.serializers import ModelSerializer 
from ..models import Biscuits

class BiscuitsSerializer(ModelSerializer):
    class Meta:
        model = Biscuits
        fields = '__all__'