from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    def validate_password(self, value: str):
        return make_password(value)

    class Meta:
        model = CustomUser
        fields = ("id", "email", "date_joined", "phone", "password", "organisation", "is_active")
        # extra_kwargs = {"password": {"write_only": True}}