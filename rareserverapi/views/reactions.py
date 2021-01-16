from rest_framework.viewsets import ModelViewSet
from rareserverapi.models import Reaction
from rareserverapi.serializers import ReactionSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


# Creates a read only permission which allows 'GET', 'OPTIONS', or 'HEAD' HTTP actions (i.e. SAFE_METHODS)
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer

    # Allow admin users (user.is_staff == True) ALL permissions
    # otherwise, regular users are read only per above permission
    permission_classes = [IsAdminUser | ReadOnly]
