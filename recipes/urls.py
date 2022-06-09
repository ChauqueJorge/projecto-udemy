from django.urls import path
from recipes.views import home, sobre, contactos



urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contactos/', contactos),
]