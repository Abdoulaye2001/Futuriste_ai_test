# Generated by Django 5.0.6 on 2024-07-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_datas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(default='img/banner/banner_1.jpg', upload_to='static/img/banner/'),
        ),
    ]
