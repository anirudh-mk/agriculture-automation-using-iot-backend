import uuid
from django.db.models import F, Value
from rest_framework import serializers
from .models import User, Farm, UserFarmLink, Vegetable, FarmVegetableLink


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "password"
        ]

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data['username'] = validated_data['email']
        return User.objects.create_user(**validated_data)

    # def validate_password(self, password):
    #     if password == self.initial_data.get('confirm_password'):
    #         return password
    #     raise serializers.ValidationError('Passwords does not match')


class FarmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = [
            'name',
            'description',
            'location'
        ]

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
            if FarmVegetableLink.objects.filter(farm_id=data['id']):
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
    vegetable = serializers.SerializerMethodField()
    # days_remaining = serializers.SerializerMethodField()

    class Meta:
        model = UserFarmLink
        fields = [
            'id',
            'farm_name',
            'vegetable'
        ]

    def get_vegetable(self,obj):

        vegetable = {}
        if obj.farm.farm_vegetable_link_farm.first() is not None:
            vegetable['name'] = obj.farm.farm_vegetable_link_farm.first().vegetable.name
            vegetable['time_require'] = obj.farm.farm_vegetable_link_farm.first().vegetable.time_required
        return vegetable


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


from .models import UserFarmLink


class FarmVegetableCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmVegetableLink
        fields = [
            'farm',
            'vegetable'
        ]

    def create(self, validate_data):
        user_farm_link_id = validate_data['farm']  # Assuming frontend sends user_farm_link id as farm
        user_farm_link = UserFarmLink.objects.filter(id=user_farm_link_id).first()
        farm_id = user_farm_link.farm
        validate_data['farm'] = farm_id
        return FarmVegetableLink.objects.create(**validate_data)

