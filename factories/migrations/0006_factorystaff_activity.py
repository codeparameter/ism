# Generated by Django 5.0.7 on 2024-07-23 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factories', '0005_staff_activity_seeder'),
    ]

    operations = [
        migrations.AddField(
            model_name='factorystaff',
            name='activity',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='factories.staffactivity'),
        ),
    ]