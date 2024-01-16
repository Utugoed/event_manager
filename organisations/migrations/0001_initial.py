# Generated by Django 5.0.1 on 2024-01-14 13:01

import organisations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=6, validators=[organisations.models.validate_postcode])),
            ],
        ),
    ]