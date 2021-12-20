from django.contrib import admin
from django.urls import path, include
from info.views import teamAPIView,formatAPIView,socialsview,teamAPIcrud,tournamentcrudAPIView,formatcrud,socialscrud
from info.views import home, PlayerAPIView, ViewPlayer, CreatePlayer, updatePlayer,deletePlayer, apiOverview,tournamentAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('overview/', apiOverview, name='apiOverview'),


    path('tournament-crudlist/<int:pk>/',tournamentcrudAPIView.as_view(),name='tournament-list'),
    path('tournament-list/',tournamentAPIView.as_view(),name='tournament-list'),


    path('team-view/',teamAPIView.as_view(),name='team-view'),
    path('team-crudview/<int:pk>/',teamAPIcrud.as_view(),name='team-view'),


    path('format-view/',formatAPIView.as_view(),name='format-view'),
    path('format-crudview/<int:pk>/',formatcrud.as_view(),name='format-view'),

    path('socials-view/',socialsview.as_view(),name='format-view'),
    path('socials-crudview/<int:pk>/',socialscrud.as_view(),name='format-view'),




    path('player-list/',PlayerAPIView.as_view(), name='player-list'),
    path('player-detail/<int:pk>/', ViewPlayer, name='player-detail'),
    path('player-create/', CreatePlayer, name='player-create'),
    path('player-update/<int:pk>/', updatePlayer, name='player-update'),
    path('player-delete/<int:pk>/', deletePlayer, name='player-delete'),
 
   
]
