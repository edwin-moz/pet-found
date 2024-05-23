from rest_framework import permissions, serializers, status, viewsets
from rest_framework.response import Response
from api.models import PetBehavior, Post
from datetime import datetime

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            "id",
            "contact_email",
            "date_added",
            "pet_behavior",
            "pet_age",
            "pet_breed",
            "pet_color",
            "pet_description",
            "pet_favorite_snack",
            "pet_image_url",
            "pet_name",
        )

class PostViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        data = request.data

        contact_email = data.get("contact_email")
        date_added = datetime.now()
        pet_behavior_id = data.get("pet_behavior")
        pet_age = data.get("pet_age")
        pet_breed = data.get("pet_breed")
        pet_color = data.get("pet_color")
        pet_description = data.get("pet_description")
        pet_favorite_snack = data.get("pet_favorite_snack")
        pet_image_url = data.get("pet_image_url")
        pet_name = data.get("pet_name")

        if (contact_email == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_behavior_id == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_age == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_breed == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_color == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_description == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_favorite_snack == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_image_url == None): return Response(status=status.HTTP_400_BAD_REQUEST)
        if (pet_name == None): return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            pet_behavior = PetBehavior.objects.get(pk=pet_behavior_id)

            post = Post.objects.create(
                contact_email = contact_email,
                date_added = date_added,
                pet_behavior = pet_behavior,
                pet_age = pet_age,
                pet_breed = pet_breed,
                pet_color = pet_color,
                pet_description = pet_description,
                pet_favorite_snack = pet_favorite_snack,
                pet_image_url = pet_image_url,
                pet_name = pet_name
            )

            serialized = PostSerializer(post, many=False)

            return Response(serialized.data, status=status.HTTP_201_CREATED)

        except PetBehavior.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        if (pk == None): return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            post = Post.objects.get(pk=pk)

            post.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Post.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        posts = Post.objects.all()

        serialized = PostSerializer(posts, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        if (pk == None): return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            post = Post.objects.get(pk=pk)

            serialized = PostSerializer(post, many=False)

            return Response(serialized.data, status=status.HTTP_200_OK)
        
        except Post.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        if (pk == None): return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data

        try:
            post = Post.objects.get(pk=pk)

            serialized = PostSerializer(data=data)

            if serialized.is_valid():
                post.contact_email = serialized.validated_data["contact_email"]
                post.pet_behavior = serialized.validated_data["pet_behavior"]
                post.pet_age = serialized.validated_data["pet_age"]
                post.pet_breed = serialized.validated_data["pet_breed"]
                post.pet_color = serialized.validated_data["pet_color"]
                post.pet_description = serialized.validated_data["pet_description"]
                post.pet_favorite_snack = serialized.validated_data["pet_favorite_snack"]
                post.pet_image_url = serialized.validated_data["pet_image_url"]
                post.pet_name = serialized.validated_data["pet_name"]

                serialized = PostSerializer(post, many=False)

                post.save()

                return Response(None, status=status.HTTP_204_NO_CONTENT)
            
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Post.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)