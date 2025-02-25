from django.urls import path
from . import views
from .views import list_books, RegistrationView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('book_list/', views.list_books, name = "book list"),
    path('library_details/', views.LibraryDetailView.as_view(), name= 'details'),
    path('register/', views.RegistrationView.as_view(), name = 'SignUp'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]