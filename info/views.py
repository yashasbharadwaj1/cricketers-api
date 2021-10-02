from django.shortcuts import render
from .models import  tournament,Player
from rest_framework import generics
from .serializer import playerserializer
class PlayerAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = playerserializer


