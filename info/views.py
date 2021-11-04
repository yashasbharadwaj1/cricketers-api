from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import  tournament,Player,Team,gameformat
from rest_framework import generics,permissions
from .serializer import playerserializer,teamSerializer,gameformatSerializer,tournamentSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'team_list':'/team-list/<int:id>/',
        'List': '/player-list/',
        'Detail View': '/player-detail/<int:id>/',
        'Create': '/player-create/',
        'Update': '/player-update/<int:id>/',
        'Delete': '/player-detail/<int:id>/',
        
    }
    return Response(api_urls)

class PlayerAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = playerserializer
class teamAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = teamSerializer
class tournamentAPIView(generics.ListAPIView):
    queryset = tournament.objects.all()
    serializer_class = tournamentSerializer
class formatAPIView(generics.ListAPIView):
    queryset = gameformat.objects.all()
    serializer_class = gameformatSerializer  
@api_view(['GET'])
def ViewPlayer(request, pk):
    player = Player.objects.get(id=pk)
    serializer = playerserializer(player, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreatePlayer(request):

    serializer = playerserializer(data=request.data)
    

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updatePlayer(request, pk):
   
    playerupdate = Player.objects.get(id=pk)
    serializer = playerserializer(instance=playerupdate, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    player.delete()
    return Response('Items delete successfully!')
