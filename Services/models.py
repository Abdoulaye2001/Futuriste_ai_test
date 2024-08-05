from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Services(models.Model):
        services_h1 = models.CharField(max_length=300, default='Nos services')
        services_span = models.CharField(max_length=200, default='Découvrez Nos Services')
        services_icon = models.ImageField(upload_to='img/service/', blank=True)
        services_title = models.CharField(max_length=300)
        services_brief = models.CharField(max_length=200)
        services_p1 = models.TextField()
        services_p2 = models.TextField()
        services_p3 = models.TextField()
        services_p4 = models.TextField()
        services_sous_titre = models.CharField(max_length=300)
        services_liste1 = models.TextField()
        services_liste2 = models.TextField()
        services_liste3 = models.TextField()
        services_liste4 = models.TextField()
        services_liste5 = models.TextField()
        services_liste6 = models.TextField()
        services_faq_title1 = models.CharField(max_length=300)
        services_faq_content1 = models.TextField()
        services_faq_title2 = models.CharField(max_length=300)
        services_faq_content2 = models.TextField()
        services_faq_title3 = models.CharField(max_length=300)
        services_faq_content3 = models.TextField()
        slug = models.SlugField()
        
        def __str__(self):
                return self.services_title
        def get_absolute_url(self):
               return reverse("services_detail", kwargs={"slug": self.slug})
        def save(self, *args, **kwargs):
                if not self.slug: 
                    self.slug = slugify(self.services_title)
                return super().save(*args, **kwargs)