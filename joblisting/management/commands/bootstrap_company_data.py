import json
from pathlib import Path
from django.core.management.base import BaseCommand

from joblisting.models import Company, Job

WORKING_DIR = Path('')

class Command(BaseCommand):
    help = 'Bootstrap company data from JSON to the database'

    def handle(self, *args, **kwargs):
        with open(WORKING_DIR / 'bootstrap_data' / 'company_data.json') as file:
            data = json.load(file)
            for entry in data:
                Company.objects.create(

                )