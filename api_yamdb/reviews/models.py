from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User

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
        verbose_name="Название произведения")
    year = models.IntegerField(
        verbose_name="Дата выхода",
        validators=[validate_year])
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст отзыва")
    score = models.SmallIntegerField(
        verbose_name="Оценка",
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        ),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации отзыва",
        db_index=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='unique review'
            )]
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст отзыва")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации отзыва",
        db_index=True)

    def __str__(self):
        return self.text
