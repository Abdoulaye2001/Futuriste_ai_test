# Generated by Django 5.0.6 on 2024-07-20 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['post_day']},
        ),
    ]