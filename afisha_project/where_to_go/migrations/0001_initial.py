# Generated by Django 3.2.16 on 2022-12-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('imgs', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description_short', models.TextField(verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Длинное описание')),
                ('coordinates_lng', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('coordinates_lat', models.FloatField(blank=True, verbose_name='Широта')),
            ],
        ),
    ]
