from django.shortcuts import render
from django.views import generic
from django.urls import reverse
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'Wowinternet/Index.html'

class ContactView(generic.TemplateView):
    template_name = 'Wowinternet/Contact.html'

class ServiciosView(generic.TemplateView):
    template_name = 'Wowinternet/Servicios.html'
