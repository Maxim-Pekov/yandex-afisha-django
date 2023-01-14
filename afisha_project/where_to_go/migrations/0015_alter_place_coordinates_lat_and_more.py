# Generated by Django 4.1.4 on 2023-01-12 11:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go', '0014_alter_place_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coordinates_lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, null=True, verbose_name='Короткое описание'),
        ),
    ]
