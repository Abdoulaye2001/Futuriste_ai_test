# Generated by Django 5.0.6 on 2024-08-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0010_devisform'),
    ]

    operations = [
        migrations.AddField(
            model_name='devisform',
            name='adress',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
