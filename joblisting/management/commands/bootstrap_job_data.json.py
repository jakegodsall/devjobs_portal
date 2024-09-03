import json
from pathlib import Path
from django.core.management.base import BaseCommand

from joblisting.models import Company, Job

WORKING_DIR = Path('')


class Command(BaseCommand):
    help = 'Bootstrap job data from JSON to the database'

    def handle(self, *args, **kwargs):
        with open(WORKING_DIR / 'bootstrap_data' / 'job_data.json') as file:
            data = json.load(file)
            for job in data:
                Job.objects.create(
                    position=job['position'],
                    role=job['role'],
                    level=job['level'],
                    posted_at=
                )