from django.urls import path
from .views import NotificationAPIView

urlpatterns = [
    path("notifications/", NotificationAPIView.as_view(), name="notifications")
]
