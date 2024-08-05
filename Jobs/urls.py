from django.urls import path
from Jobs.views import Emploi, Emploi_detail

urlpatterns = [
    path('emploi', Emploi, name='emploi'),
    path('emploi_detail/<slug>', Emploi_detail, name='emploi_detail'),
]