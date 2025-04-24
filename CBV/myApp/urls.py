# Import necessary modules for URL routing
from django.urls import path 
from . import views  # Import views from the current app

# Define URL patterns for different pages
urlpatterns = [
    # Home page view (renders static content or handles basic interactions)
    path('', views.HomeView.as_view(), name="home"),

    # Retrieves a list of all books from the database
    path('books/', views.BookListView.as_view(), name='book_list'),

    # Displays details for a specific book identified by its primary key (pk)
    # Django DetailView requires 'pk' in the URL pattern by default
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),

    # Provides an update form to modify details of a specific book
    path('book/update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),

    # Displays a confirmation page before deleting a book entry
    path('book/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),

    # Provides a form to create a new book entry
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
]
