# Generated by Django 3.2.16 on 2022-12-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go', '0003_alter_place_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='images / %Y-%m-%d/', verbose_name='Изображение'),
        ),
    ]