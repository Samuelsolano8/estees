from django.urls import path

from . import views


app_name = 'Wowinternet'
urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
    path('Contactenos/', views.ContactView.as_view(),name='Contact'),
    path('Servicios/', views.ServiciosView.as_view(),name='Servicios'),
]