# Generated by Django 5.0.7 on 2024-07-22 07:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_remove_phone_v_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='v_code',
            field=models.CharField(default='0000', max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='v_code'),
        ),
    ]
