from django.urls import path
from Projects.views import Projects, Projects_detail

urlpatterns = [
    path('realisations', Projects, name='realisations'),
    path('realisations_detail/<slug>', Projects_detail, name='realisations_detail'),
]
