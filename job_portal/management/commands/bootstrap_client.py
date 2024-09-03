from pathlib import Path
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.db import connection

from users.models import UserProfile, Client


class Command(BaseCommand):
    help = 'Bootstrap the Client table from a JSON file'

    def handle(self, *args, **options):
        file_path = settings.BASE_DIR / 'data' / 'bootstrap_client.json'

        try:
            # Delete all Client instances and their associated UserProfiles
            Client.objects.all().delete()

            with open(file_path, 'r') as file:
                data = json.load(file)

                for client in data:
                    username = client['username']
                    password = client['password']
                    first_name = client['first_name']
                    last_name = client['last_name']
                    avatar = client['avatar']
                    cv = client['cv']

                    # Create the UserProfile instance
                    user_profile = UserProfile.objects.create(
                        username=username,
                        password=make_password(password),
                        user_type=UserProfile.Type.CLIENT,
                    )

                    # Create the Client instance
                    Client.objects.create(
                        profile=user_profile,
                        first_name=first_name,
                        last_name=last_name,
                        avatar=avatar,
                        cv=cv
                    )

                    self.stdout.write(self.style.SUCCESS(f'Successfully created client {first_name} {last_name}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))
