from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from Jobs.models import Jobs
from Services.models import Services

# Create your views here.

def Emploi(request):
        emplois = Jobs.objects.all()
        emploi_count = emplois.all().count()
        paginator = Paginator(emplois, 6)
        page_number = request.GET.get('page')
        emplois = paginator.get_page(page_number)
        services = Services.objects.all()
        context = "Futuriste-Ai --Jobs"
        return render(request, '../Templates/career.html', {'context': context, 'emplois' : emplois, 'emploi_count' : emploi_count, 'services' : services})


def Emploi_detail(request, slug):
        emplois = get_object_or_404(Jobs, slug=slug)
        emplois = Jobs.objects.get(slug=slug)
        context = "Futuriste-Ai -- Jobs Détails"
        services = Services.objects.all()
        return render(request, '../Templates/career-details.html', {'context' : context, 'emplois' : emplois, 'services' : services})