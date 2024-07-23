# Generated by Django 5.0.7 on 2024-07-21 00:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='v_code',
            field=models.CharField(default='0000', max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='v_code'),
        ),
    ]