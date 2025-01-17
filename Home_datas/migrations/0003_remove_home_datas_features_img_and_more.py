# Generated by Django 5.0.6 on 2024-07-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_datas', '0002_alter_banner_banner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_datas',
            name='features_img',
        ),
        migrations.RemoveField(
            model_name='home_datas',
            name='features_span',
        ),
        migrations.RemoveField(
            model_name='home_datas',
            name='features_titre',
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(default='img/banner/banner_1.jpg', upload_to='img/banner'),
        ),
        migrations.AlterField(
            model_name='home_datas',
            name='about_h_ceo_img',
            field=models.ImageField(blank=True, default='img/about/ceo.jpg', upload_to='img/about/'),
        ),
    ]
