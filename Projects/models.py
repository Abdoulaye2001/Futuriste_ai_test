from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Categories_portfolio(models.Model):
        categorie_name = models.CharField(max_length=200)
        categorie_section = models.CharField(max_length=255)
        def __str__(self):
              return self.categorie_name

class Portfolio(models.Model):
        portfolio_img = models.ImageField(upload_to='img/portfolio/', default='static/img/portfolio/1.jpg')
        portfolio_date = models.DateField(auto_now=True)
        portfolio_title = models.CharField(max_length=300, default='#')
        categorie = models.ForeignKey(Categories_portfolio, related_name='categorie', null=True, on_delete=models.CASCADE)
        client = models.CharField(max_length=300, default='#')
        client_detail = models.CharField(max_length=500, default='#')
        client_demande = models.CharField(max_length=300, default='#')
        client_demande1 = models.CharField(max_length=300, default='#')
        equipe_name = models.CharField(max_length=600, default='#')
        equipe_job = models.CharField(max_length=600, default='#')
        equipe_name1 = models.CharField(max_length=600, default='#')
        equipe_job1 = models.CharField(max_length=600, default='#')
        portfolio_h5 = models.CharField(max_length=1000, default='#')
        portfolio_p = models.TextField(default='#')
        portfolio_p1 = models.TextField(default='#')
        portfolio_p2 = models.TextField(default='#')
        portfolio_video_img = models.ImageField(upload_to='img/portfolio/', default='static/img/portfolio/video-img.jpg')
        portfolio_link = models.CharField(max_length=500, default='#')
        portfolio_p3 = models.TextField(default='#')
        portfolio_img_projects = models.ImageField(upload_to='img/gallery/', blank=True)
        portfolio_img_title = models.CharField(max_length=255, default='#')
        portfolio_img_projects1 = models.ImageField(upload_to='img/gallery/', blank=True)
        portfolio_img_title1 = models.CharField(max_length=255, default='#')
        portfolio_img_projects2 = models.ImageField(upload_to='img/gallery/', blank=True)
        portfolio_img_title2 = models.CharField(max_length=255, default='#')
        portfolio_img_projects3 = models.ImageField(upload_to='img/gallery/', blank=True)
        portfolio_img_title3 = models.CharField(max_length=255, default='#')
        portfolio_img_projects4 = models.ImageField(upload_to='img/gallery/', blank=True)
        portfolio_img_title4 = models.CharField(max_length=255, default='#')
        portfolio_img_projects5 = models.ImageField(upload_to='img/gallery/', blank=True)
        portfolio_img_title5 = models.CharField(max_length=255, default='#')
        slug = models.SlugField(null=False, unique=True)
        def __str__(self):
                return self.portfolio_title
        def get_absolute_url(self):
               return reverse("realisations_detail", kwargs={"slug": self.slug})
        def save(self, *args, **kwargs):
                if not self.slug: 
                    self.slug = slugify(self.portfolio_title)
                return super().save(*args, **kwargs)