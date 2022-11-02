from rest_framework import serializers
from datetime import date


from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="slug",
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field="slug",
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Title
        fields = ('name', 'category', 'genre', 'year', 'description')

    def validate_year(self, value):
        year = date.today().year
        if value > year:
            raise serializers.ValidationError(
                'Проверьте дату выхода произведения')
        return value
