# Generated by Django 4.1.4 on 2023-02-09 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_remove_predresults_classification"),
    ]

    operations = [
        migrations.DeleteModel(name="PredResults",),
        migrations.DeleteModel(name="Staff",),
    ]
