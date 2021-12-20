from django.contrib import admin
from . import models
admin.site.register(models.gameformat)
admin.site.register(models.Team)
admin.site.register(models.Player)
admin.site.register(models.tournament)
admin.site.register(models.Social_life)