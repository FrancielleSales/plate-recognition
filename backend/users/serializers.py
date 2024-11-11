from django.contrib.auth.hashers import make_password  # Função para criptografar a senha
from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, value):
            raise ValidationError("Por favor, forneça um email válido.")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        
        # Encrypt password manually
        password = validated_data['password']
        user.password = make_password(password)
        
        user.save()

        return user