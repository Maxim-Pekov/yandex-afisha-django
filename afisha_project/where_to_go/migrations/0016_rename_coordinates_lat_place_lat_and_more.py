# Generated by Django 4.1.4 on 2023-01-12 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go', '0015_alter_place_coordinates_lat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='coordinates_lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='coordinates_lng',
            new_name='lng',
        ),
    ]