from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pairings
from .serializers.common import PairingSerializer

class PairingListView(ListCreateAPIView):
    queryset = Pairings.objects.all()
    serializer_class = PairingSerializer

class PairingDetailView(RetrieveUpdateDestroyAPIView):
        queryset = Pairings.objects.all()
        seriaizer_class = PairingSerializer