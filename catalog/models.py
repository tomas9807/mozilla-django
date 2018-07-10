from django.db import models
from django.urls import reverse
# Create your models here.
import uuid
#culo
class Author(models.Model):
    first_name = models.CharField(max_length=20,null=False)
    second_name = models.CharField(max_length=20,null=False)
    date_of_birth= models.DateField(null=False)
    date_of_death= models.DateField(null=True,blank=True)
    def __str__(self):
        return f'{self.first_name},{self.second_name}'
    class Meta:
        ordering = ['second_name','first_name']

class Genre(models.Model):
    name = models.CharField(max_length=20,help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)')
    def __str__(self):
        return self.name

class Lenguage(models.Model):
    name = models.CharField(max_length=20,help_text='name of the lenguage')
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=20,help_text='Title of the book')
    author = models.ForeignKey(Author,on_delete = models.SET_NULL,null=True)
    summary = models.TextField(max_length=200,help_text=' summary for this book')
    genre = models.ManyToManyField(Genre,help_text='genre of this book')
    isbn = models.CharField(max_length=20,help_text='isbn of this book')
    lenguage = models.ForeignKey(Lenguage,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title
    def display_genre(self):
        return ','.join([genre.name for genre in self.genre.all()]) 
    # def get_absolute_url(self):
    #     return reverse('book-detail',args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=20,help_text='imprint')
    due_back = models.DateField(null=True,blank=True)
    LOAD_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1,choices=LOAD_STATUS,default='m',help_text='book availability')
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id}:{self.book}'


    