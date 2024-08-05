from django.contrib import admin
from Pages.models import Clients, Terms_mono, Terms_multi, ContactForm, SiteConfiguration, DevisForm

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
        list_display = ("nom", "message", "email")

admin.site.register(Clients)
admin.site.register(Terms_mono)
admin.site.register(Terms_multi)
admin.site.register(DevisForm)
admin.site.register(ContactForm, ContactAdmin)
@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
        list_display = ("coming_soon_active",)