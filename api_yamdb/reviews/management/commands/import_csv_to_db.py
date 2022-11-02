from django.core.management.base import BaseCommand
import csv
from django.utils import timezone


class Command(BaseCommand):
    help = 'import data csv file to table on DB'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write(f"Текущее время: {time}")
