from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models



class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = models.BookInstance
    template_name = 'catalog/loaned_books.html'
    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower__exact=self.request.user).order_by('due_back')


# Create your views here.
def generate_context(**kwargs):
    context = {}
    for k,v in kwargs.items():
        context[k] = v
    return context


        


def index(request):
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    request.session.modified = True
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = models.BookInstance.objects.filter(status__exact='a').count()
    num_authors = models.Author.objects.all().count()

    return render(request,
    'catalog/index.html',
    generate_context(num_books=num_books,num_authors=num_authors,num_instances=num_instances,num_instances_available=num_instances_available,num_visits=num_visits)
    )

class BookListView(generic.ListView):
    model = models.Book
    context_object_name = 'my book list'
    queryset = models.Book.objects.all()
    template_name = 'catalog/books/book_list.html'
    paginate_by = 5
class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'catalog/books/book_detail.html'

class AuthorListView(generic.ListView):
    model = models.Author
    queryset = models.Author.objects.all()
    context_object_name = 'my author list'
    template_name = 'catalog/authors/author_list.html'
    paginate_by = 5
class AuthorDetailView(generic.DetailView):
    model = models.Author
    template_name = 'catalog/authors/author_detail.html' 