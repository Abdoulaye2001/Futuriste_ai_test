from django.contrib import admin
from .models import Portfolio, Categories_portfolio

# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
        list_display = ("portfolio_title", "portfolio_img", "portfolio_date")
        prepopulated_fields = {"slug": ("portfolio_title",)}

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Categories_portfolio)