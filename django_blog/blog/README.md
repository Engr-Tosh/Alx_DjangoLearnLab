# Authentication System Documentation

## Overview
This authentication system provides user registration, login, logout, and profile management functionalities using Django's built-in authentication system.

## Features
- **User Registration**: Allows new users to create an account.
- **User Login**: Handled by Django’s built-in authentication system.
- **User Logout**: Logs users out of their session.
- **User Profile Management**: Allows logged-in users to update their email.
- **Access Control**: Restricts profile access to authenticated users only.

## Components

### 1. User Registration
- **Class:** `SignUpView`
- **Type:** Class-Based View (CBV)
- **Functionality:**
  - Uses Django's `UserCreationForm` to create a new user.
  - Redirects users to the login page after successful registration.
  - Renders the `blog/register.html` template.

#### How to Test:
1. Navigate to the registration page (`/register/`).
2. Fill out the registration form with a username and password.
3. Submit the form.
4. Ensure the user is created and redirected to the login page.
5. Try logging in with the new credentials.

---

### 2. User Logout
- **Class:** `LogoutView`
- **Type:** Class-Based View (CBV)
- **Functionality:**
  - Logs out the authenticated user.
  - Renders a logout confirmation page.

#### How to Test:
1. Log in as an authenticated user.
2. Navigate to the logout page (`/logout/`).
3. Ensure the user is logged out.
4. Try accessing the profile page; it should redirect to the login page.

---

### 3. User Profile
- **Class:** `ProfileView`
- **Type:** Class-Based View (CBV)
- **Functionality:**
  - Restricts access to authenticated users using `LoginRequiredMixin`.
  - Displays the user's profile information.
  - Allows users to update their email.

#### How to Test:
1. Log in as an authenticated user.
2. Navigate to the profile page (`/profile/`).
3. Verify the profile details are displayed.
4. Enter a new email and submit the form.
5. Ensure the email is updated in the database.

---

## URL Configuration
Ensure that your `urls.py` file is correctly configured to route authentication views:

```python
from django.urls import path
from .views import SignUpView, LogoutView, ProfileView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
```

## Template Files
Ensure you have the following template files in `blog/templates/blog/`:
- `register.html` – For user registration
- `login.html` – For user login
- `profile.html` – Displays and updates user profile
- `logout.html` – Confirms user logout

## Dependencies
- Django 4.x or higher
- Python 3.x

## Final Notes
- Ensure `LOGIN_URL` is set in `settings.py`:
  ```python
  LOGIN_URL = '/login/'
  LOGIN_REDIRECT_URL = '/profile/'
  LOGOUT_REDIRECT_URL = '/login/'
  ```
- Run `python manage.py migrate` before testing.
- Use Django’s admin panel to verify user creation and updates.

This completes the authentication system setup and documentation.

