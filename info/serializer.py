from rest_framework import serializers
from .models import gameformat,Player,tournament,Team
class playerserializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'  
class gameformatSerializer(serializers.ModelSerializer):
    class Meta:
        model = gameformat
        fields = '__all__'  
class tournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = tournament
        fields = '__all__'                    