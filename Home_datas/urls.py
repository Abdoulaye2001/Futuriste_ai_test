from django.urls import path
from Home_datas.views import index, About_us

urlpatterns = [
    path('', index, name='home'),
    path('about', About_us, name='about')
]
