from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'phone_number', 'created_at', 'activated', 'preferences')


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'phone_number', 'preferences')


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
