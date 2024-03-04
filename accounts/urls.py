from django.urls import path
from accounts.views import SignupView, SigninView, SignoutView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("signin/", SigninView.as_view()),
    path("signout/", SignoutView.as_view()),
]
