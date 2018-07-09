from django.contrib import admin
from . import models

#classes
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('second_name','first_name','date_of_birth', 'date_of_death')

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ('title','author','summary','display_genre','isbn','lenguage')

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Lenguage)
class LenguageAdmin(admin.ModelAdmin):
    pass



