# Generated by Django 5.0.6 on 2024-07-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_datas', '0003_remove_home_datas_features_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_team_img', models.ImageField(blank=True, default='img/team/team1.jpg', upload_to='img/team/')),
                ('h_team_name', models.CharField(max_length=300)),
                ('h_team_fonction', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_review_img', models.ImageField(blank=True, default='img/testimonial/client1.jpg', upload_to='img/team/')),
                ('h_review_h', models.CharField(default='#', max_length=300)),
                ('h_review_p', models.CharField(default='#', max_length=300)),
                ('h_review_name', models.CharField(default='#', max_length=200)),
                ('h_review_fonction', models.CharField(default='#', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_feature_img',
            field=models.ImageField(blank=True, default='img/about/signature.png', upload_to='img/about/'),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_feature_link',
            field=models.CharField(default='#', max_length=500),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_feature_p',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_feature_span',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_feature_titre',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_h1',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_h1_1',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_h1_2',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_h1_3',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_p',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_p1',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_p2',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_p3',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='home_datas',
            name='h_force_titre',
            field=models.CharField(default='#', max_length=300),
        ),
    ]
