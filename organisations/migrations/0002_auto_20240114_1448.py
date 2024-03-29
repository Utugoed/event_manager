# Generated by Django 5.0.1 on 2024-01-14 14:48

from django.db import migrations

from organisations.models import Organisation


def gen_default_organisation(apps, schema_editor):
    default_organisation = Organisation.objects.create(title="Superusers")
    default_organisation.description = "Default superusers organisation"
    default_organisation.address = "No address"
    default_organisation.postcode = "999999"

    default_organisation.save()

class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(gen_default_organisation),
    ]
