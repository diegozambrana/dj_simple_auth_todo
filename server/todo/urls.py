from django.urls import path
from .views import TodoViewSet

urlpatterns = [
    path('/', TodoViewSet.as_view({'get': 'retrieve', 'post': 'update'}), name='register'),
]
