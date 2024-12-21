from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()