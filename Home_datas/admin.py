from django.contrib import admin
from .models import Banner, home_datas, Team, Testimonials, contactIndex, About_Us

# Register your models here.

admin.site.register(Banner)
admin.site.register(home_datas)
admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(contactIndex)
admin.site.register(About_Us)