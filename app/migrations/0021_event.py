# Generated by Django 3.2 on 2021-05-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_new_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('bannerimage', models.ImageField(upload_to='eventMedia')),
                ('image1', models.ImageField(upload_to='eventMedia')),
                ('image2', models.ImageField(upload_to='eventMedia')),
                ('image3', models.ImageField(upload_to='eventMedia')),
                ('image4', models.ImageField(upload_to='eventMedia')),
                ('body', models.TextField()),
            ],
        ),
    ]
