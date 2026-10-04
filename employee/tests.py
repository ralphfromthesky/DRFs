from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from employers.models.models import Employers
from employee.models.model import Employee


class EmployeeAPITest(APITestCase):

    def setUp(self):
        # Tumatakbo ito BAGO ang bawat test. Dito ihahanda ang data.
        self.employer = Employers.objects.create(
            owner="Juan",
            company_name="Acme",
            office_address="Manila",
        )
        self.url = '/employee/newEmployee/'

    def test_create_employee(self):
        # Arrange
        data = {
            "name": "Pedro",
            "salary": 25000,
            "employer": self.employer.id,
        }
        # Act
        response = self.client.post(self.url, data, format='json')
        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.first().name, "Pedro")

    def test_create_employee_without_name_fails(self):
        data = {"salary": 25000, "employer": self.employer.id}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 0)

    def test_list_employees(self):
        Employee.objects.create(name="Pedro", employer=self.employer)
        Employee.objects.create(name="Maria", employer=self.employer)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


# Create your tests here.
