from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Post


class Pokaz(ListView):
    model = Post
    template_name = 'One.html'