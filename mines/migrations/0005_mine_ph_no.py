# Generated by Django 5.0.7 on 2024-07-15 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mines', '0004_mine_activity'),
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mine',
            name='ph_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='phones.phone'),
            preserve_default=False,
        ),
    ]
