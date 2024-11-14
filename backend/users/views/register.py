from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from users.serializers.register import UserRegisterSerializer
from users.models.users import User

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = 'Usuário criado com sucesso!'
        return response
