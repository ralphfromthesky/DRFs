from ..models.models import Item
from rest_framework import serializers

class ItemSerializers(serializers.Serializer):
    class Meta:
        model = Item
        fields = ['id', 'item', 'descriptions', 'quantity', 'price']
        read_only_fields = ['id']