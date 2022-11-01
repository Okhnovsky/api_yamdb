from django.contrib import admin


from .models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'year', 'description')
    # filter_horizontal = ['genres']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
