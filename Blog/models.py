from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Categories(models.Model):
       cat_section = models.CharField(max_length=200)
       cat_name = models.CharField(max_length=300)
       def __str__(self):
              return self.cat_name

class Posts(models.Model):
        post_img = models.ImageField(upload_to='img/blog/', blank=True)
        post_title = models.CharField(max_length=300)
        categorie = models.ForeignKey(Categories, related_name='categorie', null=True,on_delete=models.CASCADE)
        post_day = models.DateField()
        post_author = models.CharField(max_length=200, default="Admin-Futuriste AI")
        post_bref = models.CharField(max_length=100)
        post_p1 = models.TextField()
        post_link1 = models.CharField(max_length=500, default="#")
        post_link1_content = models.CharField(max_length=200)
        post_p2 = models.TextField()
        post_link2 = models.CharField(max_length=500, default="#")
        post_link2_content = models.CharField(max_length=200)
        post_img_detail = models.ImageField(upload_to='img/blog/', default='static/img/blog/blog-detail.jpg')
        post_p3 = models.TextField()
        post_p4 = models.TextField()
        post_quote = models.TextField()
        post_p5 = models.TextField()
        post_link3 = models.CharField(max_length=500, default="#")
        post_link3_content = models.CharField(max_length=200)
        post_author_principal = models.CharField(max_length=200, default='#')
        post_author_desc = models.TextField(default='#')
        slug = models.SlugField(null=False, unique=True)
        class Meta:
              ordering = ['post_day']
        def __str__(self):
                return self.post_title
        def get_absolute_url(self):
               return reverse("blog_detail", kwargs={"slug": self.slug})
        def save(self, *args, **kwargs):
                if not self.slug: 
                    self.slug = slugify(self.post_title)
                return super().save(*args, **kwargs)


class Comment(models.Model):
       content = models.TextField(null=True, default='#')
       author = models.CharField(max_length=255)
       email = models.CharField(max_length=255)
       created_at = models.DateTimeField(auto_now_add=True)
       article = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='comments')
       parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
       class Meta:
              ordering = ['created_at']
       def __str__(self):
              return f"commenté par {self.author}"