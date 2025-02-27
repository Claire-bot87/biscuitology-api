from .common import BiscuitsSerializer
from biscuits.serializers.common import BiscuitsSerializer

class PopulatedReviewSerializer(BiscuitsSerializer):
    biscuit = BiscuitsSerializer(many=True)