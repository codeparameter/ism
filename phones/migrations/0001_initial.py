# Generated by Django 5.0.6 on 2024-07-13 01:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='No')),
            ],
        ),
    ]
