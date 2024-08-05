from django.urls import path
from  Pages.views import login, signup, contact, faq, clients, terms, Thank_you, coming_soon, Devis, Confirmation

urlpatterns = [
    path('login', login, name='login'),
    path('sign-up', signup, name='sign-up'),
    path('faq', faq, name='faq'),
    path('clients', clients, name='clients'),
    path('contact', contact, name='contact'),
    path('thanks/<int:unique_id>', Thank_you, name='thanks'),
    path('terms', terms, name='terms'),
    path('coming_soon', coming_soon, name='coming_soon'),
    path('devis/', Devis, name='devis'),
    path('devis_confirmé/', Confirmation, name='devis_confirmé')
]
