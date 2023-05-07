from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index_page'),
    path('reserv/', views.ReservationView, name='reserv_page'),
    path('contact/', views.contact, name='contact_us'),
]

