from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.
def generate_context(**kwargs):
    context = {}
    for k,v in kwargs.items():
        context[k] = v
    return context


def index(request):
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = models.BookInstance.objects.filter(status__exact='a').count()
    num_authors = models.Author.objects.all().count()

    return render(request,
    'catalog/index.html',
    generate_context(num_books=num_books,num_authors=num_authors,num_instances=num_instances,num_instances_available=num_instances_available)
    )

class BookListView(generic.ListView):
    model = models.Book
    context_object_name = 'my book list'
    queryset = models.Book.objects.all()
    template_name = 'catalog/books/book_list.html'
    