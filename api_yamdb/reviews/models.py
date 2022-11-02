from django.db import models


from .validators import validate_year


class Category(models.Model):
    """Category type of work"""
    name = models.CharField(max_length=256, verbose_name="Название категории")
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Слаг категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Genre of work"""
    name = models.CharField(max_length=256, verbose_name="Название жанра")
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Слаг жанра"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles'
    )
    name = models.CharField(
        max_length=256,
        verbose_name="Название произведения"
    )
    year = models.IntegerField(
        verbose_name="Дата выхода",
        validators=[validate_year]
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
