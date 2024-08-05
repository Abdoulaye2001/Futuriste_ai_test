from django.contrib import admin
from Jobs.models import Jobs

# Register your models here.
class JobsAdmin(admin.ModelAdmin):
        list_display = ("job_title", "job_price", "job_location")
        prepopulated_fields = {"slug": ("job_title",)}

admin.site.register(Jobs, JobsAdmin)