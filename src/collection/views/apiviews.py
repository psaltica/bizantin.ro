from rest_framework.views import APIView
from rest_framework.response import Response

from collection.models import Author
from collection.serializers import AuthorSerializer

class AuthorAPI(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serialized = AuthorSerializer(authors, many=True)
        return Response(serialized.data)
