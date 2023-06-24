from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import ValidationError


User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def validate(self, attrs):
        username_exits = User.objects.filter(
            username=attrs["username"]).exists()

        if username_exits:
            raise ValidationError("User with this username already exists")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)

        user.set_password(password)
        user.save()

        return user
