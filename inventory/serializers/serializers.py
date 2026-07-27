from ..models.models import Item
from rest_framework import serializers

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item', 'description', 'quantity', 'price']
        read_only_fields = ['id']