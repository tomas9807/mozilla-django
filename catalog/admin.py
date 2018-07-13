from django.contrib import admin
from . import models

class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
#classes
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('second_name','first_name','date_of_birth', 'date_of_death')
    fields = ['first_name','second_name',('date_of_birth','date_of_death')]

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ('title','author','summary','display_genre','isbn','lenguage')
    inlines = [BookInstanceInline]

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','due_back','status','borrower')
    list_filter = ('status','due_back')
    fieldsets = (
        (None,{
            'fields':('book','imprint')
        }),
        ('Availability', {
            'fields': ('status','due_back','borrower')
        })
    )
    
   

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Lenguage)
class LenguageAdmin(admin.ModelAdmin):
    pass



