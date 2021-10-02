
from django.contrib import admin
from django.urls import path
from info.views import PlayerAPIView,Listview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PlayerAPIView.as_view(), name='player-api-view'),
    path('home/', Listview.as_view(), name='home'),

  ]
