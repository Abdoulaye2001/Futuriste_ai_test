# Generated by Django 5.0.6 on 2024-07-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_posts_post_img_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_img',
            field=models.ImageField(blank=True, upload_to='img/blog/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_img_detail',
            field=models.ImageField(default='static/img/blog/blog-detail.jpg', upload_to='img/blog/'),
        ),
    ]