from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from reviews.models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer
from .mixins import CreateDeleteListViewSet


class CategoryViewSet(CreateDeleteListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)


class GenreViewSet(CreateDeleteListViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category__slug', 'genre__name', 'name', 'year')
