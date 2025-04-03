"""API routes"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentViewSet,
    PostFeedView,
    LikePostAPIView,
    UnlikePostAPIView
)

router = DefaultRouter()
router.register(r"post_all", PostViewSet, basename="post_all")
router.register(r"comment_all", CommentViewSet, basename="comment_all")

urlpatterns = [
    path('', include(router.urls)),
    path("feed/", PostFeedView.as_view(), name="feeds"),
    path("posts/<int:pk>/like/", LikePostAPIView.as_view, name="like_post"),
    path("posts/<int:pk>/unlike/", UnlikePostAPIView.as_view(), name="unlike_post")
]