# Generated by Django 4.2.15 on 2024-08-11 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='price',
            new_name='price_per_night',
        ),
    ]
