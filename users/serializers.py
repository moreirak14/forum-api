from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from users.models import UserAccount


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["first_name", "last_name", "email", "password"]

    def validate(self, data):
        user = UserAccount(**data)
        password = data.get("password")

        try:
            validate_password(password=password, user=user)
        except ValidationError as error:
            serializers_errors = serializers.as_serializer_error(error)
            raise ValidationError(
                {"password": serializers_errors["non_field_errors"]}
            ) from error

        return data

    def create(self, validated_data):
        return UserAccount.objects.create_user(**validated_data)


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["first_name", "last_name", "email"]
