from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.auth.serializer import EmailSerializer, PasswordSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

UserModel = get_user_model()


class MeView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class RecoveryPasswordRequestView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.register_email(user)
        return Response({'detail': 'check your email'}, status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user: User = JWTService.validate_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response({'detail': 'password was changed'}, status.HTTP_200_OK)
