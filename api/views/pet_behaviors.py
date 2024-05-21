from rest_framework import permissions, serializers, status, viewsets
from rest_framework.response import Response
from api.models import PetBehavior

class PetBehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetBehavior
        fields = (
            "id",
            "behavior",
        )

class PetBehaviorViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    
    def list(self, request):
        pet_behaviors = PetBehavior.objects.all()

        serialized = PetBehaviorSerializer(pet_behaviors, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)