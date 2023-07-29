# tests.py

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Place

class CreatePlaceTestCase(APITestCase):
    def test_create_place(self):
        place_data = {
            'name': 'Test Place',
            'description': 'This is a test place.',
            'latitude': 12.345,
            'longitude': -67.890,
        }
        response = self.client.post('/api/places/', place_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.count(), 1)

class RetrievePlaceTestCase(APITestCase):
    def setUp(self):
        self.place_data = {
            'name': 'Test Place',
            'description': 'This is a test place.',
            'latitude': 12.345,
            'longitude': -67.890,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_retrieve_place(self):
        response = self.client.get(f'/api/places/{self.place.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.place_data['name'])

class UpdatePlaceTestCase(APITestCase):
    def setUp(self):
        self.place_data = {
            'name': 'Test Place',
            'description': 'This is a test place.',
            'latitude': 12.345,
            'longitude': -67.890,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_update_place(self):
        updated_data = {
            'name': 'Updated Place',
            'description': 'This is an updated place.',
            'latitude': 34.567,
            'longitude': -45.678,
        }
        response = self.client.put(f'/api/places/{self.place.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.place.refresh_from_db()
        self.assertEqual(self.place.name, updated_data['name'])
        self.assertEqual(self.place.description, updated_data['description'])
        self.assertEqual(self.place.latitude, updated_data['latitude'])
        self.assertEqual(self.place.longitude, updated_data['longitude'])

class DeletePlaceTestCase(APITestCase):
    def setUp(self):
        self.place_data = {
            'name': 'Test Place',
            'description': 'This is a test place.',
            'latitude': 12.345,
            'longitude': -67.890,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_delete_place(self):
        response = self.client.delete(f'/api/places/{self.place.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Place.objects.count(), 0)
