# Generated by Django 5.0.6 on 2024-07-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='clients_span',
            field=models.CharField(default='1000', max_length=100),
        ),
        migrations.AlterField(
            model_name='clients',
            name='clients_title',
            field=models.CharField(default='Clients Satisfaits', max_length=255),
        ),
    ]