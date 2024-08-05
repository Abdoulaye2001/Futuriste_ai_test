from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Jobs(models.Model):
        job_time = models.CharField(max_length=200)
        job_title = models.CharField(max_length=300)
        job_location = models.CharField(max_length=200)
        job_price = models.CharField(max_length=300)
        job_date = models.DateField(auto_now=True)
        job_info_title = models.CharField(max_length=300, default="Information sur l'offre d'emploi")
        job_info_p = models.TextField(default="Rétrouvez ci-dessous les informations nécessaires pour pouvoir postuler à cette offre d'emploi.")
        job_h5 = models.CharField(max_length=200, default='#')
        job_li = models.TextField(max_length=300, default='#')
        job_li1 = models.TextField(max_length=300, default='#')
        job_li2 = models.TextField(max_length=300, default='#')
        job_li3 = models.TextField(max_length=300, default='#')
        job_li4 = models.TextField(max_length=300, default='#')
        job_li5 = models.TextField(max_length=300, default='#')
        job_li6 = models.TextField(max_length=300, default='#')
        job_li7 = models.TextField(max_length=300, default='#')
        job_h51 = models.CharField(max_length=200, default='#')
        job_li8 = models.TextField(max_length=300, default='#')
        job_li9 = models.TextField(max_length=300, default='#')
        job_li10 = models.TextField(max_length=300, default='#')
        job_li11 = models.TextField(max_length=300, default='#')
        job_li12 = models.TextField(max_length=300, default='#')
        job_li13 = models.TextField(max_length=300, default='#')
        job_li14 = models.TextField(max_length=300, default='#')
        job_li15 = models.TextField(max_length=300, default='#')
        job_h4 = models.CharField(max_length=200, default='#')
        job_img = models.ImageField(upload_to='img/career/', default='static/img/career/gr1.png')
        job_h6 = models.CharField(max_length=200, default='#')
        job_p = models.TextField(default='#')
        job_img1 = models.ImageField(upload_to='img/career/', default='static/img/career/gr1.png')
        job_h61 = models.CharField(max_length=200, default='#')
        job_p1 = models.TextField(default='#')
        job_img2 = models.ImageField(upload_to='img/career/', default='static/img/career/gr1.png')
        job_h62 = models.CharField(max_length=200, default='#')
        job_p2 = models.TextField(default='#')
        job_img3 = models.ImageField(upload_to='img/career/', default='static/img/career/gr1.png')
        job_h63 = models.CharField(max_length=200, default='#')
        job_p3 = models.TextField(default='#')
        job_img4 = models.ImageField(upload_to='img/career/', default='static/img/career/gr1.png')
        job_h64 = models.CharField(max_length=200, default='#')
        job_p4 = models.TextField(default='#')
        video_link = models.CharField(max_length=500, default='#')
        slug = models.SlugField(null=False, unique=True)
        def __str__(self):
                return self.job_title
        def get_absolute_url(self):
               return reverse("emploi_detail", kwargs={"slug": self.slug})
        def save(self, *args, **kwargs):
                if not self.slug: 
                    self.slug = slugify(self.job_title)
                return super().save(*args, **kwargs)