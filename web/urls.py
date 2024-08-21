from django.urls import path
from web.views import index, about, welcome, contact

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenidos/', welcome, name='welcome'),
    path('contact/', contact, name='contacto'),
]