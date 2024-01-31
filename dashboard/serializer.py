import uuid
from django.db.models import F, Value
from rest_framework import serializers
from .models import User, Farm, UserFarmLink, Vegetable, FarmVegetableLink


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


class ListAllUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'username',
            'profile_pic'
        ]


class UserDetailsSerializer(serializers.ModelSerializer):
    farms = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'profile_pic',
            'farms'
        ]

    def get_farms(self, obj):
        farm = Farm.objects.filter(
            user_farm_link_farm__user=obj
        ).values(
            'id',
            'name',
            'description',
            'location',
        )

        for data in farm:
            vegetable = Vegetable.objects.filter(
                farm_vegetable_link_vegetable__farm_id=data['id']
            ).values(
                'id',
                'name',
                'n',
                'p',
                'k',
                'time_required'
            )

            data['vegetable'] = vegetable[0]

        return farm


class ListAllVegetablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vegetable
        fields = [
            'id',
            'name',
            'n',
            'p',
            'k',
            'time_required',
        ]


class UserFarmListSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name')
    vegetable_name = serializers.SerializerMethodField()
    days_remaining = serializers.SerializerMethodField()

    class Meta:
        model = UserFarmLink
        fields = [
            'id',
            'farm_name',
            'vegetable_name',
            'days_remaining',
        ]

    def get_vegetable_name(self, obj):
        return obj.farm.farm_vegetable_link_farm.first().vegetable.name

    def get_days_remaining(self, obj):

        return obj.farm.farm_vegetable_link_farm.first().vegetable.time_required


class VegetableCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vegetable
        fields = [
            'name',
            'n',
            'p',
            'k',
            'time_required',
        ]

    def create(self, validate_data):
        validate_data['id'] = uuid.uuid4()
        return Vegetable.objects.create(**validate_data)

