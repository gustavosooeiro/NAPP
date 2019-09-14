from rest_framework import viewsets, mixins

from .models import Tag
from .serializers import TagSerializer

class TagViewSet(viewsets.GenericViewSet, 
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Manage tags in the database"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        """Return objects ordered by name"""
        return self.queryset.all().order_by('name')

    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save()
