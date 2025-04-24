# Import necessary modules for views and models
from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from . import models
from django.urls import reverse_lazy

# ----------------------- Working Without Models -----------------------

class HomeView(View):
    """ 
    Handles both GET and POST requests for the home page.
    GET: Renders a static home page with predefined data.
    POST: Retrieves user input from an HTML form and returns an HTTP response.
    """

    def get(self, request):
        # Context data to pass to the template
        data = {
            'message': 'This is the home page',
            'creator': 'Me'
        }
        return render(request, 'home.html', data)  # Render template with data
    
    def post(self, request):
        # Retrieves user input from an HTML form
        user_input = request.POST.get('user_input')  
        return HttpResponse(f"You entered: {user_input}")  # Display user input

# ----------------------- Working With Models -----------------------

class BookListView(ListView):
    """
    Retrieves a list of books from the database and passes them to the template.
    Automatically handles querying and pagination if required.
    """
    model = models.Book  # Specifies the model from which to fetch data
    template_name = 'books.html'  # Defines the template used for rendering
    context_object_name = 'books'  # Renames default queryset variable for better clarity
    paginate_by = 10  # Limits to 10 books per page


class BookDetailView(DetailView):
    """
    Displays detailed information about a single book based on its primary key (pk).
    Automatically fetches the object and passes it to the template.
    """
    model = models.Book  # Model for retrieving a single book instance
    template_name = "book_detail.html"  # Template used for rendering
    context_object_name = 'book'  # Makes the queried object accessible as 'book' in the template


class BookUpdateView(UpdateView):
    """
    Provides an update form for modifying book details.
    Handles form validation and database updates automatically.
    """
    model = models.Book  # Model whose objects can be updated
    fields = ['title', 'author', 'published_date']  # Specifies editable fields
    template_name = 'book_form.html'  # Template for rendering the update form
    success_url = reverse_lazy('book_list')  # Redirects to the book list upon successful update


class BookDeleteView(DeleteView):
    """
    Provides a confirmation page for deleting a book.
    Automatically deletes the selected book upon user confirmation.
    """
    model = models.Book  # Specifies the model containing deletable objects
    template_name = 'book_confirm_delete.html'  # Template used for the confirmation page
    success_url = reverse_lazy('book_list')  # Redirects to the book list after successful deletion
class BookCreateView(CreateView):
    """
    This view provides a form for creating a new book entry.
    Automatically handles form validation and saving data to the database.
    """
    model = models.Book
    fields = ['title', 'author', 'published_date']  # Fields to include in the form
    template_name = 'book_form.html'  # Template for rendering the form
    success_url = reverse_lazy('book_list')  # Redirect after successful creation
