from django.db import IntegrityError
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)        

        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"detail": "Successfull register."}, status=201)
            except IntegrityError as e:
                raise ValidationError({"detail": "Integrity Error: " + str(e)})
        return Response(serializer.errors, status=400)

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username,
            'email': token.user.email,
        })


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if both fields are present
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # tried to authenticate the user with the credentials provided.
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # If authentication is successful, log out.        
        logout(request)

        # response with a successful message
        return Response({"message": "Successful logout."}, status=status.HTTP_200_OK)
