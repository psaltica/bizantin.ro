from rest_framework.views import APIView
from rest_framework.response import Response

from collection.models import Author, MusicalText, Publication, Performance
from collection.serializers import *

class AuthorAPI(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serialized = AuthorSerializer(authors, many=True)
        return Response(serialized.data)


class AuthorDetailAPI(APIView):
    def get(self, request, author_id, format=None):
        author = Author.objects.get(id=author_id)
        serialized = AuthorSerializer(author)
        return Response(serialized.data)


class MusicalTextAPI(APIView):
    def get(self, request, format=None):
        print(request.query_params)
        texts = MusicalText.objects.all()
        serialized = MusicalTextSerializer(texts, many=True)
        return Response(serialized.data)


class MusicalTextDetailAPI(APIView):
    def get(self, request, text_id, format=None):
        text = MusicalText.objects.get(id=text_id)
        serialized = MusicalTextSerializer(text)
        return Response(serialized.data)


class PerformanceAPI(APIView):
    def get(self, request, format=None):
        performances = Performance.objects.all()
        serialized = PerformanceSerializer(performances, many=True)
        return Response(serialized.data)


class PerformanceDetailAPI(APIView):
    def get(self, request, performance_id, format=None):
        performance = Performance.objects.get(id=performance_id)
        serialized = PerformanceSerializer(performance)
        return Response(serialized.data)


class PublicationAPI(APIView):
    def get(self, request, format=None):
        publications = Publication.objects.all()
        serialized = PublicationSerializer(publications, many=True)
        return Response(serialized.data)


class PublicationDetailAPI(APIView):
    def get(self, request, publication_id, format=None):
        publication = Publication.objects.get(id=publication_id)
        serialized = PublicationSerializer(publication)
        return Response(serialized.data)
