
from django.contrib import admin
from django.urls import path
from info.views import PlayerAPIView,ViewPlayer,CreatePlayer,updatePlayer,deletePlayer,apiOverview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apiOverview, name='apiOverview'),
    path('player-list/', PlayerAPIView.as_view(), name='player-list'),
    path('player-detail/<int:pk>/', ViewPlayer, name='player-detail'),
    path('player-create/', CreatePlayer, name='player-create'),
    path('player-update/<int:pk>/', updatePlayer, name='player-update'),
    path('player-delete/<int:pk>/', deletePlayer, name='player-delete'),
  ]
