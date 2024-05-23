from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from .models import CustomUser



class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        existing_user = CustomUser.objects.filter(
            email=validated_data["email"]
        )
        if existing_user.exists():
            raise serializers.ValidationError(
                {"email": "Email already exists."}
            )
        
        user = CustomUser.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["email"]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        breakpoint()
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
