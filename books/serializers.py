from rest_framework import serializers
from . import models

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookCategory
        fields = '__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    
    class Meta:
        model = models.Book
        fields = '__all__'
        extra_fields = ['genre_name']
        
        
class BorrowerSerializer(serializers.ModelSerializer):
    #name = serializers.StringRelatedField(many=False)
    #book = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Borrower
        fields = '__all__'
        
        
class WishlistSerializer(serializers.ModelSerializer):
    # name = serializers.StringRelatedField(many=False)
    # book = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Wishlist
        fields = '__all__'