from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import SignUpSerializer, GenTokenSerializer
from users.models import User


class APISignUp(APIView):
    """
    Получение кода подтверждения на заранее
    переданный email.
    """

    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=[data['to_email']]
        )
        email.send()

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        email_body = (
            f'Добро пожаловать, {user.username}!'
            f'Ваш код доступа: {user.confirmation_code}'
        )
        data = {
            'email_subject': 'Код доступа',
            'email_body': email_body,
            'to_email': user.email,
        }
        self.send_email(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class APIGenToken(APIView):
    """
    Получение JWT токена
    """

    def post(self, request):
        serializer = GenTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        confirmation_code = serializer.validated_data['confirmation_code']
        user = get_object_or_404(User, username=username)
        if confirmation_code == user.confirmation_code:
            token = str(AccessToken.for_user(user))
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(
            {'confirmation_code': 'Неверный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST
        )
