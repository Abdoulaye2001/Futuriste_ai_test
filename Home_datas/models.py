from django.db import models

# Create your models here.

class Banner(models.Model):
        banner_image = models.ImageField(upload_to='img/banner', default='img/banner/banner_1.jpg')
        banner_span = models.CharField(max_length=200)
        banner_titre = models.CharField(max_length=200)
        banner_link = models.CharField(max_length=500, blank=True)
        def __str__(self):
            return self.banner_titre
        
class home_datas(models.Model):
       about_h_ceo_img = models.ImageField(upload_to='img/about/', blank=True, default='img/about/ceo.jpg')
       about_h_video_link = models.CharField(max_length=1000, default="#")
       about_h_span = models.CharField(max_length=200, default="#")
       about_h_titre = models.CharField(max_length=200, default="#")
       about_h_p1 = models.TextField(default="#")
       about_h_p2 = models.TextField(default="#")
       about_img = models.ImageField(upload_to='img/about/', blank=True)
       about_ceo_name = models.CharField(max_length=200, default="#")
       about_ceo_fonction = models.CharField(max_length=200, default="#")
       h_feature_img = models.ImageField(upload_to='img/feature/', blank=True, default='img/about/signature.png')
       h_feature_link = models.CharField(max_length=500, default="#")
       h_feature_titre = models.CharField(max_length=300, default="#")
       h_feature_p = models.CharField(max_length=300, default="#")
       h_feature_span = models.CharField(max_length=300, default="#")
       h_force_titre = models.CharField(max_length=300, default="#")
       h_force_h1 = models.CharField(max_length=300, default="#")
       h_force_p = models.CharField(max_length=300, default="#")
       h_force_h1_1 = models.CharField(max_length=300, default="#")
       h_force_p1 = models.CharField(max_length=300, default="#")
       h_force_h1_2 = models.CharField(max_length=300, default="#")
       h_force_p2 = models.CharField(max_length=300, default="#")
       h_force_h1_3 = models.CharField(max_length=300, default="#")
       h_force_p3 = models.CharField(max_length=300, default="#")
       def __str__(self):
            return self.about_h_titre

class About_Us(models.Model):
      about_img = models.ImageField(upload_to='img/about/', blank=True,)
      about_link = models.CharField(max_length=500)
      about_titre = models.CharField(max_length=200, default="#")
      about_p1 = models.TextField(default="#")
      about_p2 = models.TextField(default="#")
      about_img1 = models.ImageField(upload_to='img/about/', blank=True)
      about_ceo_name = models.CharField(max_length=200, default="#")
      about_ceo_fonction = models.CharField(max_length=200, default="#")
      about_h2 = models.CharField(max_length=255, default='#')
      about_p3 = models.TextField(default='#')
      about_p4 = models.TextField(default='#')
      about_h2_1 = models.CharField(max_length=255, default='#')
      about_p5 = models.TextField(default='#')
      about_li = models.TextField(default='#')
      about_li1 = models.TextField(default='#')
      about_li2 = models.TextField(default='#')
      about_li3 = models.TextField(default='#')
      about_li4 = models.TextField(default='#')
       

class Team(models.Model):
       h_team_img = models.ImageField(upload_to='img/team/', blank=True, default='img/team/team1.jpg')
       h_team_name = models.CharField(max_length=300)
       h_team_fonction = models.CharField(max_length=300)
       def __str__(self):
            return self.h_team_name
       

class Testimonials(models.Model):
       h_review_img = models.ImageField(upload_to='img/team/', blank=True, default='img/testimonial/client1.jpg')
       h_review_h = models.CharField(max_length=300, default="#")
       h_review_p = models.TextField(default="#")
       h_review_name = models.CharField(max_length=200, default="#")
       h_review_fonction = models.CharField(max_length=200, default="#")
       def __str__(self):
            return self.h_review_name
       

class contactIndex(models.Model):
      name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      phone = models.CharField(max_length=255)
      def __str__(self):
            return f"contacté par {self.name}"