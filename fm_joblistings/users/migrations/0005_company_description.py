# Generated by Django 5.0.2 on 2024-04-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_client_profile_alter_company_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
