from rest_framework import serializers
from ..models.models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author_name',
            'published_date',
            'description',
            'is_available',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']