# Generated by Django 4.2.4 on 2023-09-12 23:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_tickettype_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='max_number_to_issue',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
