from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

# Serializers
from .serializers.common import BiscuitsSerializer 

# Models
from .models import Biscuits

# Create your views here.

class BiscuitListView(APIView):
    pass

 



#* /biscuits/:biscuit_id - GET show, PUT update, DELETE delete
class BiscuitDetailView(APIView):
    pass
  