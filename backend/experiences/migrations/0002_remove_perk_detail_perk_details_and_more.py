# Generated by Django 4.2.15 on 2024-08-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perk',
            name='detail',
        ),
        migrations.AddField(
            model_name='perk',
            name='details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
