# Generated by Django 5.0.6 on 2024-07-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_img_detail',
            field=models.ImageField(default='static/img/blog/blog-detail.jpg', upload_to='static/img/blog/'),
        ),
    ]