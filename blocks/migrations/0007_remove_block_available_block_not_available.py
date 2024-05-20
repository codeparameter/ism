# Generated by Django 5.0.6 on 2024-05-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0006_auto_20240517_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='available',
        ),
        migrations.AddField(
            model_name='block',
            name='not_available',
            field=models.BooleanField(db_default=False),
        ),
    ]