from django.test import TestCase
from .models import Tender

class TenderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Tender.objects.create(
            name='Test tender',
            description='This is a test tender',
            category='Test category',
            euro_value='100.00',
        )

    def test_created_at_field(self):
        tender = Tender.objects.get(pk=1)
        field_label = tender._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_name_field(self):
        tender = Tender.objects.get(pk=1)
        field_label = tender._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_field(self):
        tender = Tender.objects.get(pk=1)
        field_label = tender._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_category_field(self):
        tender = Tender.objects.get(pk=1)
        field_label = tender._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_euro_value_field(self):
        tender = Tender.objects.get(pk=1)
        field_label = tender._meta.get_field('euro_value').verbose_name
        self.assertEqual(field_label, 'euro value')

    def test_name_max_length(self):
        tender = Tender.objects.get(pk=1)
        max_length = tender._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_category_max_length(self):
        tender = Tender.objects.get(pk=1)
        max_length = tender._meta.get_field('category').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_name(self):
        tender = Tender.objects.get(pk=1)
        expected_object_name = f'{tender.name}'
        self.assertEqual(expected_object_name, tender.name)

    def test_tender_displayname(self):
        tender = Tender.objects.get(pk=1)
        self.assertEqual(str(tender), '#1 Test tender')

    def test_tender_has_category(self):
        tender = Tender.objects.get(pk=1)
        expected_category = f'{tender.category}'
        self.assertEqual(expected_category, 'Test category')

    def test_tender_has_price(self):
        tender = Tender.objects.get(pk=1)
        expected_price = f'{tender.euro_value}'
        self.assertEqual(expected_price, '100.00')