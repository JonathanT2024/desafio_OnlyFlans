from django.urls import path
from web.views import index, about, welcome

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenidos/', welcome, name='welcome'),
]