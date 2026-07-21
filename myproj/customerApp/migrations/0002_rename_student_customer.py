# Renames the existing table instead of deleting student data and creating a new table.
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customerApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Student",
            new_name="Customer",
        ),
    ]
