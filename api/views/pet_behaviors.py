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

    def create(self, request):
        data = request.data

        behavior = data.get("behavior")

        if (behavior == None): return Response(status=status.HTTP_400_BAD_REQUEST)

        pet_behavior = PetBehavior.objects.create(
            behavior=behavior
        )

        serialized = PetBehaviorSerializer(pet_behavior, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        if (pk == None): return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            pet_behavior = PetBehavior.objects.get(pk=pk)

            pet_behavior.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except PetBehavior.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        pet_behaviors = PetBehavior.objects.all()

        serialized = PetBehaviorSerializer(pet_behaviors, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        if (pk == None): return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            pet_behavior = PetBehavior.objects.get(pk=pk)

            serialized = PetBehaviorSerializer(pet_behavior, many=False)

            return Response(serialized.data, status=status.HTTP_200_OK)
        
        except PetBehavior.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        if (pk == None): return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data

        try:
            pet_behavior = PetBehavior.objects.get(pk=pk)

            serialized = PetBehaviorSerializer(data=data)

            if serialized.is_valid():
                pet_behavior.behavior = serialized.validated_data["behavior"]

                serialized = PetBehaviorSerializer(pet_behavior)

                pet_behavior.save()

                return Response(None, status=status.HTTP_204_NO_CONTENT)
            
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        except PetBehavior.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)