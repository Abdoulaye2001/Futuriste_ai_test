# Generated by Django 5.0.6 on 2024-07-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_img', models.ImageField(blank=True, upload_to='static/img/blog/')),
                ('post_title', models.CharField(max_length=300)),
                ('post_day', models.DateField()),
                ('post_author', models.CharField(default='Admin-Futuriste AI', max_length=200)),
                ('post_bref', models.CharField(max_length=100)),
                ('post_p1', models.TextField()),
                ('post_link1', models.CharField(default='#', max_length=500)),
                ('post_link1_content', models.CharField(max_length=200)),
                ('post_p2', models.TextField()),
                ('post_link2', models.CharField(default='#', max_length=500)),
                ('post_link2_content', models.CharField(max_length=200)),
                ('post_img_detail', models.ImageField(blank=True, upload_to='static/img/blog/')),
                ('post_p3', models.TextField()),
                ('post_p4', models.TextField()),
                ('post_quote', models.TextField()),
                ('post_p5', models.TextField()),
                ('post_link3', models.CharField(default='#', max_length=500)),
                ('post_link3_content', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]