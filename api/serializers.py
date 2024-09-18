from rest_framework import serializers
from .models import Author, Book, Favorite

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'published_date']

    # Ensure the author field is required
    def validate_author(self, value):
        if not value:
            raise serializers.ValidationError("Author ID is required.")
        return value

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'book']
