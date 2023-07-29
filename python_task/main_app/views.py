# views.py

from rest_framework import generics
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import Q


class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDeleteView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer



class CustomPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class PlaceListAPIView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = CustomPageNumberPagination



class PlaceSearchAPIView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')
        queryset = Place.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
        return queryset

