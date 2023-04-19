from django.urls import path
from .views import Pokaz

urlpatterns = [
    path('', Pokaz.as_view(), name = 'One')
]