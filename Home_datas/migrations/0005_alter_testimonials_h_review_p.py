# Generated by Django 5.0.6 on 2024-07-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_datas', '0004_team_testimonials_home_datas_h_feature_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='h_review_p',
            field=models.TextField(default='#'),
        ),
    ]
