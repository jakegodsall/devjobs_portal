import json
from django.conf import settings
from django.core.management.base import BaseCommand
from users.models import Company
from job_portal.models import Language, Tool, Job


class Command(BaseCommand):
    help = 'Bootstraps the Job table from a JSON file'

    def handle(self, *args, **options):
        file_path = settings.BASE_DIR / 'data' / 'bootstrap_jobs.json'
        try:
            with open(file_path, 'r') as file:
                jobs_data = json.load(file)

                for data in jobs_data:
                    company = Company.objects.get(company_name=data['company'])
                    job = Job.objects.create(
                        company=company,
                        position=data['position'],
                        role=data['role'],
                        level=data['level'],
                        contract=data['contract'],
                        location=data['location'],
                        salary=data['salary'],
                        is_featured=data.get('is_featured', False),
                        description=data['description'],
                        qualifications=data['qualifications'],
                        benefits=data['benefits'],
                        growth=data['growth']
                    )

                    # Adding languages
                    for lang_name in data.get('languages', []):
                        language, created = Language.objects.get_or_create(name=lang_name)
                        job.languages.add(language)

                    # Adding tools
                    for tool_name in data.get('tools', []):
                        tool, created = Tool.objects.get_or_create(name=tool_name)
                        job.tools.add(tool)

                    job.save()

                    self.stdout.write(self.style.SUCCESS(f'Successfully created job {data["position"]} at {company.company_name}'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))
