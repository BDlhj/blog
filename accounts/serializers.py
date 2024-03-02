from django.contrib.auth import password_validation
from rest_framework import serializers
from accounts.models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_check = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password_check"]
    
    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate(self, data):
        if data["password"] != data["password_check"]:
            raise serializers.ValidationError({"password_check": "Check password_check"})
        
        return data
    
    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

