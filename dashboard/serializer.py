import uuid

from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
            'phone',
            'password',
        ]

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        return User.objects.create_user(**validated_data)

    def validate_password(self, password):
        if password == self.initial_data.get('confirm_password'):
            return password
        raise serializers.ValidationError('Passwords does not match')
