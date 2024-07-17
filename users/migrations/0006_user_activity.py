# Generated by Django 5.0.7 on 2024-07-17 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_activity_seeder'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activity',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='users.activity'),
        ),
    ]
