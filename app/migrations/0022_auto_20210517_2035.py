# Generated by Django 3.2 on 2021-05-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image1',
            field=models.ImageField(blank=True, upload_to='eventMedia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image2',
            field=models.ImageField(blank=True, upload_to='eventMedia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image3',
            field=models.ImageField(blank=True, upload_to='eventMedia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image4',
            field=models.ImageField(blank=True, upload_to='eventMedia'),
        ),
    ]
