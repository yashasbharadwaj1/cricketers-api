from django.contrib import admin
from django.urls import path, include
from info.views import home
from info.views import PlayerAPIView, ViewPlayer, CreatePlayer, updatePlayer, deletePlayer, apiOverview, teamAPIView,home,tournamentAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('tournament-list',tournamentAPIView.as_view(),name='tournament-list'),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('overview/', apiOverview, name='apiOverview'),
    path('team-list/<int:pk>', teamAPIView.as_view(), name='team-list'),
    path('player-detail/<int:pk>/', ViewPlayer, name='player-detail'),
    path('player-create/', CreatePlayer, name='player-create'),
    path('player-update/<int:pk>/', updatePlayer, name='player-update'),
    path('player-delete/<int:pk>/', deletePlayer, name='player-delete'),
    #
    #
    #
   
]
