import uuid

from rest_framework import serializers
from .models import User, Farm, UserFarmLink


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        return User.objects.create_user(**validated_data)

    def validate_password(self, password):
        if password == self.initial_data.get('confirm_password'):
            return password
        raise serializers.ValidationError('Passwords does not match')


class FarmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['name']

    def create(self, validated_data):
        validated_data['id'] = (uuid.uuid4())
        farm = Farm.objects.create(**validated_data)
        if farm:
            user_id = self.initial_data.get('user_id')
            UserFarmLink.objects.create(
                id=uuid.uuid4(),
                farm=farm,
                user_id=user_id
            )
        return farm
