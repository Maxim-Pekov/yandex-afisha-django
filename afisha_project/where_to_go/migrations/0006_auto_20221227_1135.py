# Generated by Django 3.2.16 on 2022-12-27 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go', '0005_alter_image_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='places',
        ),
        migrations.AddField(
            model_name='image',
            name='places',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='where_to_go.place', verbose_name='Изображения'),
            preserve_default=False,
        ),
    ]
