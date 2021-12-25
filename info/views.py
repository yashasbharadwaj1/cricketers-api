
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import  tournament,Player,Team,gameformat,Social_life
from rest_framework import generics
from .serializer import playerserializer,teamSerializer,gameformatSerializer,tournamentSerializer,socialsSerializer

def home(request):
    return render(request,'apidata.html')

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        1:'tournament-crudlist/<int:pk>/',
        2:'tournament-list/',
        3:'team-view/',
        4:'team-crudview/<int:pk>/',
        5:'format-view/',
        6:'format-crudview/<int:pk>/',
        7:'socials-view/',
        8:'socials-crudview/<int:pk>/',
        9: 'player-list/',
       10:'player-detail/<int:pk>/', 
       11:'player-create/', 
       12:'player-update/<int:pk>/', 
      13:'player-delete/<int:pk>/'
     
    }
    return Response(api_urls)

class PlayerAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = playerserializer

class teamAPIcrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = teamSerializer  
class teamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = teamSerializer   

class tournamentcrudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tournament.objects.all()
    serializer_class = tournamentSerializer
class tournamentAPIView(generics.ListAPIView):
    queryset = tournament.objects.all()
    serializer_class = tournamentSerializer


class formatcrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = gameformat.objects.all()
    serializer_class = gameformatSerializer 
class formatAPIView(generics.ListAPIView):
    queryset = gameformat.objects.all()
    serializer_class = gameformatSerializer 



class socialscrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social_life.objects.all()
    serializer_class = socialsSerializer
class socialsview(generics.ListAPIView):
    queryset = Social_life.objects.all()
    serializer_class = socialsSerializer



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

