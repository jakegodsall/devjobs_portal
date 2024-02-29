# Generated by Django 5.0.2 on 2024-02-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joblisting', '0002_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='languages',
            field=models.ManyToManyField(blank=True, to='joblisting.language'),
        ),
        migrations.AlterField(
            model_name='job',
            name='tools',
            field=models.ManyToManyField(blank=True, to='joblisting.tool'),
        ),
    ]
