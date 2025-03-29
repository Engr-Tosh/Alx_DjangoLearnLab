# API Documentation

## Overview
This API provides endpoints for managing **Posts** and **Comments** in a Django REST Framework application. Users can create, retrieve, update, and delete posts and comments while ensuring only authors can modify their own content.

## Authentication
All requests require authentication using **Token Authentication**. Include the token in the `Authorization` header:
```
Authorization: Token your_api_token_here
```

## Endpoints

### 1. Posts
#### **Retrieve all posts**
**GET** `/api/posts/`

**Query Parameters:**
- `search`: Filter posts by title or author's username.
- `page`: Paginate results (default 10 posts per page).

**Example Request:**
```
GET /api/posts/?search=django&page=2
```

**Example Response:**
```json
{
    "count": 25,
    "next": "http://example.com/api/posts/?page=3",
    "previous": "http://example.com/api/posts/?page=1",
    "results": [
        {
            "author": "john_doe",
            "title": "Introduction to Django",
            "content": "Django is a high-level Python Web framework...",
            "created_at": "2025-03-29T12:00:00Z",
            "updated_at": "2025-03-29T12:30:00Z"
        }
    ]
}
```

#### **Retrieve a single post**
**GET** `/api/posts/{id}/`

**Example Request:**
```
GET /api/posts/1/
```

**Example Response:**
```json
{
    "author": "john_doe",
    "title": "Introduction to Django",
    "content": "Django is a high-level Python Web framework...",
    "created_at": "2025-03-29T12:00:00Z",
    "updated_at": "2025-03-29T12:30:00Z"
}
```

#### **Create a new post**
**POST** `/api/posts/`

**Request Body:**
```json
{
    "title": "Django Basics",
    "content": "This is a beginner tutorial on Django."
}
```

**Example Response:**
```json
{
    "author": "john_doe",
    "title": "Django Basics",
    "content": "This is a beginner tutorial on Django.",
    "created_at": "2025-03-29T12:45:00Z",
    "updated_at": "2025-03-29T12:45:00Z"
}
```

#### **Update a post** (Author Only)
**PUT/PATCH** `/api/posts/{id}/`

**Example Request:**
```json
{
    "content": "Updated content for the Django tutorial."
}
```

#### **Delete a post** (Author Only)
**DELETE** `/api/posts/{id}/`

---

### 2. Comments
#### **Retrieve all comments**
**GET** `/api/comments/`

#### **Retrieve comments for a specific post**
**GET** `/api/posts/{id}/comments/`

#### **Create a new comment**
**POST** `/api/comments/`

**Example Request:**
```json
{
    "post": 1,
    "content": "This is an insightful post!"
}
```

**Example Response:**
```json
{
    "post": 1,
    "author": "jane_doe",
    "content": "This is an insightful post!",
    "created_at": "2025-03-29T13:00:00Z",
    "updated_at": "2025-03-29T13:00:00Z"
}
```

#### **Update a comment** (Author Only)
**PUT/PATCH** `/api/comments/{id}/`

#### **Delete a comment** (Author Only)
**DELETE** `/api/comments/{id}/`

---

## Filtering & Pagination
- **Search by title or author username:** `/api/posts/?search=keyword`
- **Paginate results:** `/api/posts/?page=2`

---

## Permissions
- **Authenticated users** can read and create posts and comments.
- **Only authors** can update or delete their own posts/comments.

---

## Error Handling
Responses may include:
```json
{
    "detail": "You do not have permission to perform this action."
}
```

---

## Conclusion
This API enables efficient **Post and Comment management** with **search, filtering, pagination, and permissions** in Django REST Framework. Happy coding! 🚀

