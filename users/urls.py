from django.urls import path

from users.views import RegisterUserView, GetUserView

urlpatterns = [
    path("register", RegisterUserView.as_view()),
    path("me", GetUserView.as_view()),
]
