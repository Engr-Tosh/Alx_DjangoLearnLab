from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('book_list/', views.list_books, name = "book_list"),
    path('library_details/<int:pk>/', views.LibraryDetailView.as_view(), name= 'details'),
    path('register/', views.register.as_view(), name = 'register'),
    path('login/', views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # path('logout/', views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path('logout_page/', views.logout, name='logout_page')
 
]