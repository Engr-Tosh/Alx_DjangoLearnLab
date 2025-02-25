from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.list_books, name = "book list"),
    path('library_details/', views.LibraryDetailView.as_view(), name= 'details'),
    path('register/', views.Register.as_view(), name = 'register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name="logout")
]