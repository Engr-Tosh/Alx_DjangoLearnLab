# Social Media API

## Project Overview
This Django-based REST API serves as the backend for a social media platform, supporting user authentication, profile management, post creation, commenting, and following functionality. It utilizes Django REST Framework (DRF) for API implementation and token-based authentication.

## Features
- User registration and authentication (token-based authentication)
- User profile management (bio, profile picture, followers, following)
- User login/logout functionality
- Post creation, retrieval, updating, and deletion
- Commenting on posts
- Follow and unfollow functionality

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

5. **Create required Django apps**
```bash
python manage.py startapp accounts
python manage.py startapp posts
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
    'posts',
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

### 4. Follow a User
**Endpoint:** `POST /follow/`
**Description:** Allows a user to follow another user.

#### Request Body:
```json
{
    "user_id": 2
}
```

#### Response:
```json
{
    "message": "User successfully followed"
}
```

### 5. Unfollow a User
**Endpoint:** `DELETE /unfollow/`
**Description:** Allows a user to unfollow another user.

#### Request Body:
```json
{
    "user_id": 2
}
```

#### Response:
```json
{
    "message": "Successfully unfollowed"
}
```

---

## Posts and Comments Endpoints

### 6. Create a Post
**Endpoint:** `POST /posts/`
**Description:** Allows an authenticated user to create a post.

#### Request Body:
```json
{
    "title": "My First Post",
    "content": "This is the content of my first post."
}
```

#### Response:
```json
{
    "id": 1,
    "author": "example_user",
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "created_at": "2025-03-30T12:00:00Z"
}
```

### 7. Retrieve All Posts
**Endpoint:** `GET /posts/`
**Description:** Fetches a list of all posts.

#### Response:
```json
[
    {
        "id": 1,
        "author": "example_user",
        "title": "My First Post",
        "content": "This is the content of my first post.",
        "created_at": "2025-03-30T12:00:00Z"
    }
]
```

### 8. Comment on a Post
**Endpoint:** `POST /posts/{post_id}/comments/`
**Description:** Allows users to add a comment to a post.

#### Request Body:
```json
{
    "content": "Great post!"
}
```

#### Response:
```json
{
    "id": 1,
    "post": 1,
    "author": "example_user",
    "content": "Great post!",
    "created_at": "2025-03-30T12:10:00Z"
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

## Contributions
Feel free to contribute by submitting a pull request or reporting issues.

Happy Coding! 🚀

