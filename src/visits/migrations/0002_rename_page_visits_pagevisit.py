# Generated by Django 5.0.9 on 2024-11-02 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("visits", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="page_visits", new_name="PageVisit",),
    ]
