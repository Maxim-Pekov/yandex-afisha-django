# Generated by Django 4.1.4 on 2022-12-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go', '0007_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['my_order'], 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['title'], 'verbose_name': 'Метка на карте', 'verbose_name_plural': 'Метки на карте'},
        ),
        migrations.AddField(
            model_name='image',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]