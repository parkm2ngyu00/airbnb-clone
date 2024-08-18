from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Perk
from .serializers import PerkSerializer

class PerkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.perk = Perk.objects.create(
            name="Free WiFi",
            details="High-speed internet access",
            explanation="Stay connected with our complimentary WiFi service"
        )

    def test_perk_creation(self):
        self.assertTrue(isinstance(self.perk, Perk))
        self.assertEqual(self.perk.__str__(), self.perk.name)

    def test_perk_fields(self):
        self.assertEqual(self.perk.name, "Free WiFi")
        self.assertEqual(self.perk.details, "High-speed internet access")
        self.assertEqual(self.perk.explanation, "Stay connected with our complimentary WiFi service")

class PerkAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.perk = Perk.objects.create(name="Free Drinks", details="Complimentary beverages")
        self.list_url = '/api/v1/experiences/perks/'
        self.detail_url = f'/api/v1/experiences/perks/{self.perk.pk}'

    def test_get_all_perks(self):
        response = self.client.get(self.list_url)
        perks = Perk.objects.all()
        serializer = PerkSerializer(perks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_perk(self):
        data = {
            "name": "Free Parking",
            "details": "Complimentary parking for guests",
            "explanation": "Park your car worry-free during your stay"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # As per your view logic
        self.assertEqual(Perk.objects.count(), 2)
        self.assertEqual(Perk.objects.get(name="Free Parking").details, "Complimentary parking for guests")

    def test_get_single_perk(self):
        response = self.client.get(self.detail_url)
        perk = Perk.objects.get(id=self.perk.id)
        serializer = PerkSerializer(perk)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_perk(self):
        data = {"name": "Updated Free Drinks"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Perk.objects.get(id=self.perk.id).name, "Updated Free Drinks")

    def test_delete_perk(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Perk.objects.count(), 0)

    def test_invalid_perk_creation(self):
        invalid_data = {
            "name": "",  # Empty name should be invalid
            "details": "This shouldn't be created"
        }
        response = self.client.post(self.list_url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_non_existent_perk(self):
        non_existent_url = '/api/v1/experiences/perks/999'
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class PerkSerializerTest(TestCase):
    def test_perk_serializer(self):
        perk_data = {
            "name": "Test Perk",
            "details": "Test Details",
            "explanation": "Test Explanation"
        }
        serializer = PerkSerializer(data=perk_data)
        self.assertTrue(serializer.is_valid())
        perk = serializer.save()
        self.assertEqual(perk.name, "Test Perk")
        self.assertEqual(perk.details, "Test Details")
        self.assertEqual(perk.explanation, "Test Explanation")

    def test_perk_serializer_invalid_data(self):
        invalid_perk_data = {
            "name": "",  # Empty name should be invalid
            "details": "Test Details",
        }
        serializer = PerkSerializer(data=invalid_perk_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)