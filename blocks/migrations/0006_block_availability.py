# Generated by Django 5.0.7 on 2024-07-14 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0005_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='availability',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='blocks.availability'),
        ),
    ]
