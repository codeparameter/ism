# Generated by Django 5.0.7 on 2024-07-15 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phones.phone'),
        ),
    ]
