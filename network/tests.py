# network/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import NetworkNode, Contact, Product

User = get_user_model()


class NetworkNodeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='admin', password='password123', is_active_employee=True)
        self.client.force_authenticate(user=self.user)

        self.contact = Contact.objects.create(
            email='supplier@example.com',
            country='USA',
            city='New York',
            street='Main',
            house_number='123'
        )

        self.product = Product.objects.create(
            name='Product 1',
            model='Model X',
            release_date='2023-01-01'
        )

        self.supplier = NetworkNode.objects.create(
            name='Supplier',
            contact=self.contact,
            debt=100.00
        )
        self.supplier.products.add(self.product)

    def test_create_network_node(self):
        contact = Contact.objects.create(
            email='retail@example.com',
            country='USA',
            city='Los Angeles',
            street='Second',
            house_number='456'
        )
        product = Product.objects.create(
            name='Product 2',
            model='Model Y',
            release_date='2024-01-01'
        )
        data = {
            'name': 'Retail Network',
            'contact': contact.id,
            'products': [product.id],
            'supplier': self.supplier.id,
            'debt': 50.00
        }
        response = self.client.post('/api/nodes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NetworkNode.objects.count(), 2)
        created_node = NetworkNode.objects.get(name='Retail Network')
        self.assertEqual(created_node.name, 'Retail Network')

    def test_filter_network_nodes_by_country(self):
        response = self.client.get('/api/nodes/?search=USA')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_clear_debt_action(self):
        contact = Contact.objects.create(
            email='retail@example.com',
            country='USA',
            city='Los Angeles',
            street='Second',
            house_number='456'
        )
        product = Product.objects.create(
            name='Product 2',
            model='Model Y',
            release_date='2024-01-01'
        )
        node = NetworkNode.objects.create(
            name='Retail Network',
            contact=contact,
            debt=50.00,
            supplier=self.supplier
        )
        node.products.add(product)
        self.client.login(username='admin', password='password123')
        response = self.client.post('/admin/network/networknode/', {
            'action': 'clear_debt', '_selected_action': [self.supplier.id]
        })
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.debt, 0.00)
