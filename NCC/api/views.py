from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist

class Login(APIView):

    def get(self, request):
        token = request.COOKIES.get('access')
        if not token:
            return Response({'message': 'Please login!'})
        return Response({'message': 'You are logged in.'})

    def post(self, request):
        user_name = request.data.get('userName')  
        password = request.data.get('password')

        if user_name is None or password is None:
            return Response({'message': 'Invalid credentials!'}, status=400)

        try:
            user = Users.objects.get(userName=user_name)
        except ObjectDoesNotExist:
            return Response({'message': 'User not found!'}, status=404)

        if not check_password(password, user.password):
            return Response({'message': 'Invalid credentials!'}, status=400)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({'message': 'Login successful!'})
        response.set_cookie(key='access', value=access_token, httponly=True)

        return response
