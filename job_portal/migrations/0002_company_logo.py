# Generated by Django 5.0.2 on 2024-02-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.FileField(null=True, upload_to='logos/'),
        ),
    ]