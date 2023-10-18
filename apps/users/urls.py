from django.urls import path

from .views import UserCreateView

urlpatterns = [
    path('', UserCreateView.as_view(), name='users_create')
]