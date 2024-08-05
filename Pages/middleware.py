from django.shortcuts import redirect
from django.urls import reverse
from .models import SiteConfiguration


class ComingSoonMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            url = request.path
            on_admin_page = url.startswith("/admin")
            config = SiteConfiguration.objects.first()
            coming_soon_url = reverse("coming_soon")
            if config and config.coming_soon_active and request.path != coming_soon_url and on_admin_page==False:
                return redirect('coming_soon')
            response = self.get_response(request)
            return response