from django.db import migrations
from home.authorizations import authorize as au

def authorize(apps, schema_editor):
    au()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.RunPython(authorize),
    ]

