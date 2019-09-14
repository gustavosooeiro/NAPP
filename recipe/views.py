from rest_framework import viewsets, mixins

from .models import Tag, Ingredient
from .serializers import TagSerializer, IngredientSerializer


class BaseRecipeAttrViewSet(viewsets.GenericViewSet, 
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Base ViewSet for recipes"""

    def get_queryset(self):
        """Return objects ordered by name"""
        return self.queryset.all().order_by('name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()

class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
