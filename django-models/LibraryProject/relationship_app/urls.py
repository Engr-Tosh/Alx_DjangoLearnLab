from django.urls import path
from . import views
from django.contrib.auth.views import LoginView         #imports django built in view for login
from .views import LogoutView               #imports the custom created Logoutview to render te logout page

urlpatterns = [
    path('book_list/', views.list_books, name = "book_list"),
    path('library_details/<int:pk>/', views.LibraryDetailView.as_view(), name= 'details'),
    path('register/', views.register.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('admin/', views.Admin, name = "admin_page")
]