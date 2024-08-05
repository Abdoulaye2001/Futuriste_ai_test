from django.contrib import admin
from .models import Services

# Register your models here.
class servicesAdmin(admin.ModelAdmin):
        list_display = ("services_title", "services_brief")
        prepopulated_fields = {"slug": ("services_title",)}

admin.site.register(Services, servicesAdmin)
