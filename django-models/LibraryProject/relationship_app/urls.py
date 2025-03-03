from django.urls import path
from . import views
from django.contrib.auth.views import LoginView         #imports django built in view for login
from .views import LogoutView              #imports the custom created Logoutview to render te logout page
from .views import list_books
urlpatterns = [
    path('book_list/', views.list_books, name = "book_list"),
    path('library_details/<int:pk>/', views.LibraryDetailView.as_view(), name= 'details'),
    path('register/', views.register.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('admin/', views.Admin, name = "admin_page"),
    path('librarian/', views.Librarian, name="librarians_page"),
    path('add_book/', views.add_book, name = "add_book"),
    path('delete_book/', views.delete, name="delete_book"),
    path('edit_book/', views.edit, name="update_book")
]