from django.urls import path
from .views import (
    pingPublic,
    pingPrivate,
    RegistrationAPIView,
)


urlpatterns = [
    # test API ping
    path('ping_public/', pingPublic, name="ping_public"),
    path('ping_private/', pingPrivate, name="ping_private"),
    path('auth/register/', RegistrationAPIView.as_view(), name='register'),
]
