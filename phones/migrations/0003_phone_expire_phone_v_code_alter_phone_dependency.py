# Generated by Django 5.0.7 on 2024-07-20 02:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_dependency_phone_is_mobile_phone_pre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='v_code',
            field=models.CharField(default='0000', max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='v_code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='dependency',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
