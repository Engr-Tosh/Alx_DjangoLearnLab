from django.urls import path
from . import views
from .views import list_books, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('book_list/', views.list_books, name = "book list"),
    path('library_details/', views.LibraryDetailView.as_view(), name= 'details'),
    path('register/', views.register.as_view(), name = 'register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name ='login'),
    path('view.register', LogoutView.as_view(template_name="registration/logout"), name='logout')
]