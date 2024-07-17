# Generated by Django 5.0.6 on 2024-05-20 18:01

from django.db import migrations
from mines.models import Activity, statuses


def seed_activity(apps, schema_editor):
    # Activity = apps.get_model("apps", "Activity")
    for status in statuses:
        # instance = Activity.objects.create(status=status[0])
        Activity.objects.create(status=status[0])


class Migration(migrations.Migration):

    dependencies = [
        ('mines', '0002_activity_alter_mine_phone'),
    ]

    operations = [
        migrations.RunPython(seed_activity),
    ]
