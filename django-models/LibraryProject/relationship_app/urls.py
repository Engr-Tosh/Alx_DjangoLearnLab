from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('book_list/', views.list_books, name = "book_list"),
    path('library_details/<int:pk>/', views.LibraryDetailView.as_view(), name= 'details'),
    path('register/', views.register.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
]