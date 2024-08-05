from django.shortcuts import render
from .models import Banner, home_datas, Team, Testimonials, contactIndex, About_Us
from Blog.models import Posts
from Services.models import Services
from Pages.models import Clients

# Create your views here.
def index(request):
        services = Services.objects.all()
        banniere = Banner.objects.all()
        home = home_datas.objects.all()
        team = Team.objects.all()
        clients = Clients.objects.all()
        articles_recents = Posts.objects.all().order_by('-post_day')[:3]
        review = Testimonials.objects.all()
        if request.method == 'POST':
                name = request.POST.get("nom")
                email = request.POST.get('email')
                telephone = request.POST.get('tel')
                if not name or not email or not telephone:
                        raise ValueError('Tous les champs sont obligatoires.')
                new_contact = contactIndex(
                        name = name,
                        email = email,
                        phone = telephone
                )
                new_contact.save()
        return render(request, '../Templates/index.html', {'services': services, 'banniere': banniere, 'home': home, 'team': team, 'review': review, 'articles_recents': articles_recents, 'clients': clients})
def About_us(request):
        team = Team.objects.all()
        clients = Clients.objects.all()
        review = Testimonials.objects.all()
        about = About_Us.objects.all()
        services = Services.objects.all()
        context = "Futuriste Ai -- About"
        return render(request, '../Templates/about-us.html', {'context': context,'team': team, 'review': review,  'clients': clients, 'about' : about, 'services': services})