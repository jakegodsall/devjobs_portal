from pathlib import Path
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection

from job_portal.models import Tool


class Command(BaseCommand):
    help = 'Bootstrap tool data from JSON to the database'

    def handle(self, *args, **kwargs):
        file_path = Path(settings.BASE_DIR / 'data' / 'bootstrap_tools.json')
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                # delete existing rows
                Tool.objects.all().delete()
                if connection.vendor == 'sqlite':
                    sql = "DELETE FROM sqlite_sequence WHERE name = 'job_portal_tools'"
                    with connection.cursor() as cursor:
                        cursor.execute(sql)

                for tool in data:
                    Tool.objects.create(**tool)
                self.stdout.write(self.style.SUCCESS('Successfully loaded tools'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))