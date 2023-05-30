# Django management command to create dummy tenders
from django.core.management.base import BaseCommand
from tenders.models import Tender


class Command(BaseCommand):
    help = 'Creates dummy tenders'

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            Tender.objects.create(
                name=f'Test tender{i}',
                description=f'This is a test tender number {i}',
                category=f'dummy_category{i%2}',
                euro_value=f'{i*1000.00}',
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created dummy tender{i}'))