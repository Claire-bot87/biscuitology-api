from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Serializers
from .serializers.common import BiscuitsSerializer 

# Models
from .models import Biscuits

# Create your views here.

class BiscuitListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
       
        biscuits_queryset = Biscuits.objects.all()
        biscuits_serialized = BiscuitsSerializer(biscuits_queryset, many=True)
        print(biscuits_serialized.data)
        return Response(biscuits_serialized.data)
    
    
    def post(self, request):
        request.data['user'] = request.user.id
        #1. pass the request.data into the serializer for deserialization
        biscuit_serializer = BiscuitsSerializer(data=request.data)# the data key is for data that will be added
#2.check that the data is valid
        if biscuit_serializer.is_valid():
#3.if the data was valid save the model and send the created object back to the client
            biscuit_serializer.save()
            return Response(biscuit_serializer.data, 201)
    #4. if the data was in invalid, we wil send the errors back:
        return Response(biscuit_serializer.errors, 422)



#* /biscuits/:biscuit_id - GET show, PUT update, DELETE delete
class BiscuitDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, biscuit_id):
        try:
             biscuit = Biscuits.objects.get(id=biscuit_id)
             return biscuit
        except Biscuits. DoesNotExist as e:
             print(e)
             raise NotFound('Biscuit not found')
        
    #* GET show
    def get(self, request, biscuit_id):
        
        biscuit = self.get_object(biscuit_id)

        serialized_biscuit = BiscuitsSerializer(biscuit)

        return Response(serialized_biscuit.data)

      # * PUT update route
    def put(self, request, biscuit_id):
        # 1. Get the whale object
        biscuit = self.get_object(biscuit_id)

        # 2. Pass the instance above (whale) and the incoming data (request.data) into the serializer
        serialized_biscuit = BiscuitsSerializer(biscuit, data=request.data, partial=True)
        
        # 3. Validate the incoming data
        if serialized_biscuit.is_valid():
            # 4. Save the instance
            serialized_biscuit.save()
            # 5. Return the updated instance back to the client
            return Response(serialized_biscuit.data)
        
        # 6. Send the errors back in a 422
        return Response(serialized_biscuit.errors, 422)
    
       # * DELETE delete route
    def delete(self, request, biscuit_id):
        biscuit = self.get_object(biscuit_id)
        biscuit.delete()
        return Response(status=204)


 