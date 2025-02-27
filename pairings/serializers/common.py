from rest_framework import serializers
from ..models import Pairings

class PairingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pairings
        fields = '__all__'