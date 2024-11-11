from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = 'Usuário criado com sucesso!'
        return response
