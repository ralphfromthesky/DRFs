from ..models.models import Gamers
from rest_framework import serializers

class GamerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gamers
        fields = ['id', 'name', 'age', 'address', 'isPlaying']
        read_only_fields = ['id']

