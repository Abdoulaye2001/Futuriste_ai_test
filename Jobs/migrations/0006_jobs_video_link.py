# Generated by Django 5.0.6 on 2024-07-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0005_remove_jobs_job_h65_remove_jobs_job_p5'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='video_link',
            field=models.CharField(default='#', max_length=500),
        ),
    ]
