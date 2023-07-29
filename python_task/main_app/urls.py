# urls.py

from django.urls import path
from .views import PlaceListCreateView, PlaceListAPIView,  PlaceDeleteView, PlaceSearchAPIView

urlpatterns = [
    path('api/places/', PlaceListCreateView.as_view(), name='place-list-create'),
    path('api/places/delete/<int:pk>/', PlaceDeleteView.as_view(), name='place-delete'),
    path('api/places/', PlaceListAPIView.as_view(), name='place-list'),
    path('api/places/search/', PlaceSearchAPIView.as_view(), name='place-search'),
]
