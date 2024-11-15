from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models.users import User
from users.serializers.login import UserLoginSerializer

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

            if check_password(password, user.password):
                return Response({
                    "message": "Login realizado com sucesso!",
                    "user_id": user.id,
                    "user_name": user.name,
                }, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
