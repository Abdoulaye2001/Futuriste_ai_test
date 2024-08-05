from django.db import models

# Create your models here.

class Clients(models.Model):
        clients_span = models.CharField(max_length=100, default='1000')
        clients_title = models.CharField(max_length=255, default='Clients Satisfaits')
        clients_img = models.ImageField(upload_to='img/clients/', blank=True)
        clients_alt = models.CharField(max_length=300)
        clients_name = models.CharField(max_length=255)
        def __str__(self):
            return self.clients_name

class Terms_mono(models.Model):
      terms_titre = models.CharField(max_length=255)
      terms_p1 = models.TextField(default='#')
      terms_p2 =models.TextField(default='#')
      def __str__(self):
          return self.terms_titre
      

class Terms_multi(models.Model):
      terms_titre2 = models.CharField(max_length=255)
      terms_p = models.TextField(default='#')
      terms_li = models.TextField(default='#')
      terms_li1 = models.TextField(default='#')
      terms_li2 = models.TextField(default='#')
      terms_li3 = models.TextField(default='#')
      terms_li4 = models.TextField(default='#')
      terms_li5 = models.TextField(default='#')
      terms_li6 = models.TextField(default='#')
      terms_li7 = models.TextField(default='#')
      def __str__(self):
          return self.terms_titre2
    
class ContactForm(models.Model):
     nom = models.CharField(max_length=255)
     email = models.CharField(max_length=300)
     phone = models.CharField(max_length=300)
     message = models.TextField(null=True)
     id_unique = models.CharField(max_length=200, default='#')
     def __str__(self):
        return f"contacté par {self.nom}"


class SiteConfiguration(models.Model):
    coming_soon_active = models.BooleanField(default=False)
    def __str__(self):
          return "Site Configuration"
    class Meta:
         verbose_name = "Site Configuration"
         verbose_name_plural = "Site Configurations"


class DevisForm(models.Model):
     name = models.CharField(max_length=800, blank=True)
     name_compagny = models.CharField(max_length=300, blank=True)
     email = models.CharField(max_length=300, blank=True)
     adress = models.CharField(max_length=500, blank=True)
     services = models.CharField(max_length=800, blank=True)
     projects_details = models.TextField(blank=True)
     budget = models.CharField(max_length=800, blank=True)
     date_start = models.CharField(max_length=500, blank=True)
     message = models.TextField(blank=True)
     call_date = models.CharField(max_length=500, blank=True)
     phone = models.CharField(max_length=300, blank=True)
     feedbak = models.TextField(blank=True)
     identifiant = models.CharField(max_length=1000, blank=False, default="identifiant-1")
     def __str__(self):
        return f"Devis demandée par {self.name_compagny}"