from rest_framework.viewsets import ModelViewSet
from rareserverapi.models import Reaction
from rareserverapi.serializers import ReactionSerializer


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
