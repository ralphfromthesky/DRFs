from ..models.models import Items
from rest_framework import serializers

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'item_name', 'item_count', 'value', 'is_available', 'item_descriptions']
        read_only_fields = ['id']