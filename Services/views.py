from django.shortcuts import render
from django.shortcuts import get_object_or_404
from Services.models import Services
from Home_datas.models import Testimonials
# Create your views here.

def services(request):
        services = Services.objects.all()
        context = "Futuriste Ai -- Services"
        return render(request, '../Templates/services.html',{'services': services, 'context': context})
def services_detail(request, slug):
        services = get_object_or_404(Services, slug=slug)
        services = Services.objects.all()
        tous_services = services.filter(slug=slug)
        review = Testimonials.objects.all()
        context = "Futuriste Ai -- Services Detail"
        return render(request, '../Templates/services-details.html', {'services': services, 'context': context, 'tous_services' : tous_services, 'review' : review})