
import datetime 
from .models import Book, Author, BookInstance, Genre
from . forms import RenewBookForm, RenewBookModelForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect  
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.shortcuts import render, get_object_or_404 

# Create your views here. 




def books_index(request, template = 'book/book-home.html'):
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available copies of books
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_books_title_word_available = Book.objects.filter(
        title__icontains='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    #set the context
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'num_genres': num_genres,
        'num_books_title_word_available': num_books_title_word_available,
         }

    return render(request, template, context = context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    # your own name for the list as a template variable
    context_object_name = 'books'
    queryset = Book.objects.all()  # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'book/book_list.html'



class BookDetailView(generic.DetailView):
    model = Book 
    template_name = 'book/book_detail.html'


 
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'book/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class AllLoanedBooksListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    paginate_by: 25
    queryset = BookInstance.objects.filter(
        status__exact='o').order_by('due_back')
    template_name = 'book/all_borrowed_books.html'


@login_required
@permission_required('book.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
        context = {'form': form,
                   'book_instance': book_instance, }
        return render(request, 'book/book_renew_librarian.html', context)



class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 25

    # your own name for the list as a template variable
    context_object_name = 'authors'
    queryset = Book.objects.all()  # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'book/author_list.html'



class AuthorDetailView(generic.DetailView):
    model = Author 
    template_name = 'book/author_detail.html'


 
class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '11/06/2020'}
    template_name = 'book/author_form.html'


 
class AuthorUpdate(UpdateView):
    model = Author
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'
    template_name = 'book/author_form.html'

 
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
