from django.contrib import admin
from .models import Posts, Categories, Comment

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
        list_display = ("post_title", "post_bref", "post_day")
        prepopulated_fields = {"slug": ("post_title",)}

admin.site.register(Posts, PostsAdmin)
admin.site.register(Categories)
admin.site.register(Comment)