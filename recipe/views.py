from rest_framework import viewsets, mixins

from .models import Tag
from .serializers import TagSerializer

class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        self.queryset.order_by('-name')