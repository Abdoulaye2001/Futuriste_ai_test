import uuid
from django.shortcuts import render, redirect
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.sessions.models import Session
from django.urls import reverse
from Pages.models import Clients, Terms_mono, Terms_multi, ContactForm, DevisForm
from Services.models import Services

# Create your views here.

def login(request):
        context = "Futuriste Ai -- Login"
        services = Services.objects.all()
        return render(request, '../Templates/login.html', {'context': context, 'services' : services})


def signup(request):
        context = "Futuriste Ai -- SignUp"
        services = Services.objects.all()
        return render(request, '../Templates/signup.html', {'context': context, 'services' : services})


def contact(request):
        context = "Futuriste Ai -- Contact"
        services = Services.objects.all()
        clients = Clients.objects.all()
        if request.method == 'POST':
                name = request.POST.get('nom')
                email = request.POST.get('email')
                telephone = request.POST.get('tel')
                message = request.POST.get('message')
                unique_id = random.randint(100000, 999999)
                url_with_id = f'thanks/{unique_id}'
                request.session['contact_name'] = name
                request.session['contact_email'] = email
                if not name or not email or not telephone or not message:
                        raise ValueError('Tous les champs sont obligatoires.')
                new_mail = ContactForm(
                        nom = name,
                        email = email,
                        phone = telephone,
                        message = message,
                        id_unique = unique_id
                )
                new_mail.save()
                subject = f"Message de {name}"
                body = f"""
                Nom : {name}
                Email : {email}
                Téléphone : {telephone}
                Message : {message}
                """
                send_mail(subject, body, settings.EMAIL_HOST_USER, ['iammoriba12@gmail.com'])
                messages.add_message(request, messages.SUCCESS, 'Votre message a bien été envoyé.')
                return redirect(url_with_id)
        return render(request, '../Templates/contact-us.html', {'context': context, 'services' : services, 'clients': clients,})


def Thank_you(request, unique_id):
        if 'contact_name' in request.session:
                name = request.session['contact_name']
                del request.session['contact_name']
        else:
                name = None
        if 'contact_email' in request.session:
                email = request.session['contact_email']
                del request.session['contact_email']
        else:
                email = None
        context = "Futuriste Ai -- Thanks"
        services = Services.objects.all()
        return render(request, '../Templates/thank-you.html', {'context': context, 'name': name, 'email' : email, 'services' : services})


def terms(request):
        context = "Futuriste Ai -- Terms"
        terms_mono = Terms_mono.objects.all()
        terms_multi = Terms_multi.objects.all()
        services = Services.objects.all()
        return render(request, '../Templates/terms.html', {'context': context, 'terms_mono' : terms_mono, 'terms_multi' : terms_multi, 'services' : services})


def faq(request):
        context = "Futuriste Ai -- Faq"
        services = Services.objects.all()
        return render(request, '../Templates/faq.html', {'context': context, 'services' : services})


def clients(request):
        context = "Futuriste Ai -- Clients"
        clients = Clients.objects.all()
        services = Services.objects.all()
        paginator = Paginator(clients, 6)
        page_number = request.GET.get('page')
        clients = paginator.get_page(page_number)
        return render(request, '../Templates/clients.html', {'context': context, 'clients': clients, 'services' : services})

def Devis(request):
        if request.method == 'POST':
                personne = request.POST.get('nom')
                compagny = request.POST.get('compagny')
                email = request.POST.get('email')
                phone = request.POST.get('tel')
                adresse = request.POST.get('adress')
                service = request.POST.getlist('services[]')
                project = request.POST.get('projects_detail')
                budget = request.POST.get('budget')
                start_date = request.POST.get('start_date')
                message = request.POST.get('message')
                call = request.POST.get('booking')
                feedbak = request.POST.get('feedback')
                quote_number = uuid.uuid4()
                request.session['devis_name'] = personne
                request.session['devis_start_date'] = start_date
                request.session['devis_tel'] = phone
                quote = DevisForm(
                        name = personne,
                        name_compagny = compagny,
                        email = email,
                        phone = phone,
                        adress = adresse,
                        services = service,
                        projects_details = project,
                        budget = budget,
                        date_start = start_date,
                        message = message, 
                        call_date = call,
                        feedbak = feedbak,
                        identifiant = quote_number
                )
                quote.save()
                subject = f"Message de {personne}"
                body = f"""
                Entreprise : {compagny}
                Email : {email}
                Adresse : {adresse}
                Service choisi : {service}
                Téléphone : {phone}
                Project Détails : {project}
                Budget : {budget}
                date_start : {start_date}
                call_date : {call}
                feedback : {feedbak}
                Identifiant pour le devis : {quote_number}
                """
                send_mail(subject, body, settings.EMAIL_HOST_USER, ['iammoriba12@gmail.com'])
                return redirect(f'{reverse('devis_confirmé')}?email={email}&quoteNumber={quote_number}')
        return render(request, '../Templates/devis.html')

def Confirmation(request):
        email = request.GET.get('email')
        start_date = request.GET.get('start_date')
        quote_number = request.GET.get('quoteNumber')
        if 'devis_name' in request.session:
                personne = request.session['devis_name']
                del request.session['devis_name']
        else:
                personne = None
        if 'devis_tel' in request.session:
                phone = request.session['devis_tel']
                del request.session['devis_tel']
        else:
                phone = None
        if 'devis_start_date' in request.session:
                start_date = request.session['devis_start_date']
                del request.session['devis_start_date']
        else:
                start_date = None
        context = {
                'email': email,
                'personne': personne,
                'phone': phone,
                'start_date' : start_date,
                'quote_number': quote_number
        }
        return render(request, '../Templates/confirmation.html', context)

def coming_soon(request):
        return render(request, '../Templates/coming-soon.html')