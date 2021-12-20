
from django.db.models import fields
from rest_framework import serializers
from .models import gameformat,Player,tournament,Team,Social_life
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
class socialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_life
        fields = '__all__'  
          