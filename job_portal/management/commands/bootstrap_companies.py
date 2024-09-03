import json
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import UserProfile, Company


class Command(BaseCommand):
    help = 'Bootstraps the Company table from a JSON file'

    def handle(self, *args, **options):
        file_path = settings.BASE_DIR / 'data' / 'bootstrap_company.json'
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                for company in data:
                    username = company['username']
                    password = company['password']
                    company_name = company['company_name']
                    logo = company['logo']
                    location = company['location']
                    description = company['description']

                    # Create the UserProfile instance
                    user_profile = UserProfile.objects.create(
                        username=username,
                        password=make_password(password),
                        user_type=UserProfile.Type.COMPANY,
                    )

                    # Create the Company instance
                    company = Company.objects.create(
                        profile=user_profile,
                        company_name=company_name,
                        logo=logo,
                        location=location,
                        description=description
                    )

                    self.stdout.write(self.style.SUCCESS(f'Successfully created company {company_name}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))