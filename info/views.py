from django.shortcuts import render
from .models import  tournament,Player
from rest_framework import generics
from .serializer import playerserializer
from django.views.generic import ListView
class Listview(ListView):
    model = Player
    template_name = 'player_list.html'
class PlayerAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = playerserializer


