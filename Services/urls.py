from django.urls import path
from Services.views import services, services_detail

urlpatterns = [
    path('services', services, name='services'),
    path('services_detail/<slug>', services_detail, name='services_detail')
]