from rest_framework import permissions, serializers, status, viewsets
from rest_framework.response import Response
from api.models import PetBehavior, Post

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

    def list(self, request):
        posts = Post.objects.all()

        serialized = PostSerializer(posts, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)