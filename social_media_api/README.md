# Social Media API

## Project Overview
This is a Django-based REST API for a social media platform, enabling user authentication, profile management, and token-based authentication using Django REST Framework (DRF).

## Features
- User registration
- User login with token authentication
- User profile retrieval
- Custom user model with additional fields (bio, profile picture, followers)

---

## Setup Instructions

### Prerequisites
Ensure you have Python installed on your system. You can check your installation by running:
```bash
python --version
```
Install `pip`, `virtualenv`, and other dependencies:
```bash
pip install virtualenv
```

### Installation Steps
1. **Clone the repository**
```bash
git clone <repository-url>
cd social_media_api
```

2. **Create a virtual environment and activate it**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**
```bash
pip install django djangorestframework djangorestframework.authtoken
```

4. **Create a new Django project**
```bash
django-admin startproject social_media_api .
```

5. **Create an `accounts` app**
```bash
python manage.py startapp accounts
```

6. **Add required apps to `INSTALLED_APPS` in `settings.py`**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]
```

7. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

8. **Create a superuser (optional, for admin access)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin credentials.

9. **Run the server**
```bash
python manage.py runserver
```

---

## Authentication Endpoints

### 1. User Registration
**Endpoint:** `POST /register/`
**Description:** Registers a new user and generates an authentication token.

#### Request Body:
```json
{
    "username": "example_user",
    "email": "user@example.com",
    "password": "securepassword"
}
```

#### Response:
```json
{
    "username": "example_user",
    "email": "user@example.com"
}
```

### 2. User Login
**Endpoint:** `POST /login/`
**Description:** Authenticates the user and returns an authentication token.

#### Request Body:
```json
{
    "username": "example_user",
    "password": "securepassword"
}
```

#### Response:
```json
{
    "token": "generated_token_here",
    "message": "Login Successful"
}
```

### 3. User Profile
**Endpoint:** `GET /profile/`
**Description:** Retrieves the logged-in user’s profile details.
**Authentication Required:** Yes (Token-based authentication)

#### Response:
```json
{
    "id": 1,
    "username": "example_user",
    "email": "user@example.com",
    "bio": "Software developer",
    "profile_picture": null,
    "followers": []
}
```

---

## User Model Overview

The `CustomUser` model extends Django’s `AbstractUser`, adding the following fields:

```python
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)
```

- **bio**: A short user biography.
- **profile_picture**: A user profile image.
- **followers**: A ManyToMany field allowing users to follow others.

---

## Testing the API
Use Postman or cURL to test the API endpoints.

- **Example cURL Request for Login:**
```bash
curl -X POST http://127.0.0.1:8000/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "example_user", "password": "securepassword"}'
```

- **Example cURL Request for Profile:**
```bash
curl -X GET http://127.0.0.1:8000/profile/ \
  -H "Authorization: Token generated_token_here"
```

---

## Conclusion
This API provides essential authentication features for a social media application using Django REST Framework. Future enhancements can include features like password reset, user updates, and additional endpoints for social interactions.

### Contributions
Feel free to contribute by submitting a pull request or reporting issues.

Happy Coding! 🚀


