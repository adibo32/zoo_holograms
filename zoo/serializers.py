from rest_framework import serializers
from .models import Hologram

class HologramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hologram
        fields = '__all__'
