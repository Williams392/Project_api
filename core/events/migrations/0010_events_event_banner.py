# Generated by Django 4.2.4 on 2023-09-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_rename_event_type_events_e_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_banner',
            field=models.ImageField(blank=True, null=True, upload_to='event_banners/'),
        ),
    ]
