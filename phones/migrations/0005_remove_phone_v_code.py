# Generated by Django 5.0.7 on 2024-07-21 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_alter_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='v_code',
        ),
    ]
