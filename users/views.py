from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import GetUserSerializer, RegisterUserSerializer


class RegisterUserView(APIView):
    def post(self, request: Request):
        data = request.data
        serializer = RegisterUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data="Successfully", status=status.HTTP_201_CREATED)


class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user = request.user
        user = GetUserSerializer(user)

        return Response(data=user.data, status=status.HTTP_200_OK)
