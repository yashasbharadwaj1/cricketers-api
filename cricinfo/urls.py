from django.contrib import admin
from django.urls import path, include
from info.views import PlayerAPIView, ViewPlayer, CreatePlayer, updatePlayer, deletePlayer, apiOverview, teamAPIView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="cric  List API",
        default_version='v1',
        description="An api for cricketers info ",
        terms_of_service="",
        contact=openapi.Contact(email="yashasbharadwaj6@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),
    #
    #
    path('overview/', apiOverview, name='apiOverview'),
    path('team-list/<int:pk>', teamAPIView.as_view(), name='team-list'),
    path('player-detail/<int:pk>/', ViewPlayer, name='player-detail'),
    path('player-create/', CreatePlayer, name='player-create'),
    path('player-update/<int:pk>/', updatePlayer, name='player-update'),
    path('player-delete/<int:pk>/', deletePlayer, name='player-delete'),
    #
    #
   
]
