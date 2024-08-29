from django.urls import path
from web.views import index, about, welcome, contact, success

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenidos/', welcome, name='welcome'),
    path('contacto/', contact, name='contact'),
    path('exito/', success, name='success'),
] 