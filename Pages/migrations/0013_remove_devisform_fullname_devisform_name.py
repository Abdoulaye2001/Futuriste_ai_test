# Generated by Django 5.0.6 on 2024-08-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0012_rename_full_name_devisform_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devisform',
            name='fullname',
        ),
        migrations.AddField(
            model_name='devisform',
            name='name',
            field=models.CharField(blank=True, max_length=800),
        ),
    ]