from django.urls import path
from .views import RegisterFormView

urlpatterns = [
    path("", RegisterFormView.as_view(), name="register"),
]