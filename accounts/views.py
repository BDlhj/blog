from rest_framework import generics
from accounts.models import User
from accounts.serializers import SignupSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
