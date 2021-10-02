from rest_framework import serializers
from .models import gameformat,Player,tournament,Team
class playerserializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'matches_played_so_far')