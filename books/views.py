from rest_framework import filters, viewsets
from . import models, serializers

class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for common configurations.
    """
    queryset = None
    serializer_class = None

class BookCategoryViewset(BaseModelViewSet):
    """
    ViewSet for managing book categories.
    """
    queryset = models.BookCategory.objects.all()
    serializer_class = serializers.BookCategorySerializer
    
class BookViewset(BaseModelViewSet):
    """
    ViewSet for managing books.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['genre__name']
    
    def get_queryset(self):
        """
        Optionally filter books by category.
        """
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(genre_id=category_id)
        return queryset
    
class BorrowerViewset(BaseModelViewSet):
    """
    ViewSet for managing borrowers.
    """
    queryset = models.Borrower.objects.all()
    serializer_class = serializers.BorrowerSerializer

class WishlistViewset(BaseModelViewSet):
    """
    ViewSet for managing wishlists.
    """
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer
