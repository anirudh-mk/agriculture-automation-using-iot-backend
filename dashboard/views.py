from django.db.models import Q, F
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from utils.response import CustomResponse
from utils.permission import TokenGenerate, CustomizePermission

from .models import User, Farm, UserFarmLink, Vegetable
from .serializer import (UserCreateSerializer,
                         FarmCreateSerializer,
                         ListAllUsersSerializer,
                         UserDetailsSerializer,
                         ListAllVegetablesSerializer)


class CreateUserAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = UserCreateSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()

            return CustomResponse(
                general_message='User created successfully'
            ).get_success_response()

        return CustomResponse(
            response=serializer.errors
        ).get_failure_response()


class UserLoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return CustomResponse(
                general_message='email and password is required'
            ).get_failure_response()

        user = authenticate(request, email=email, password=password)

        if user:
            auth = TokenGenerate().generate(user)
            return CustomResponse(
                general_message="successfully login",
                response=auth,
            ).get_success_response()
        else:
            return CustomResponse(
                general_message="login failed"
            ).get_failure_response()


class FarmCreateAPI(APIView):
    def post(self, request):
        if request.data.get('user_id') is None:
            return CustomResponse(
                response={
                    "user_id": ["This field is required."]
                }

            ).get_failure_response()

        serializer = FarmCreateSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return CustomResponse(
                general_message='Farm created successfully'
            ).get_success_response()

        return CustomResponse(
            response=serializer.errors
        ).get_failure_response()


class ListAllUsersAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        user = User.objects.all()
        serializer = ListAllUsersSerializer(
            user,
            many=True
        )
        return CustomResponse(
            response=serializer.data
        ).get_success_response()


class UserDetailsAPI(APIView):
    authentication_classes = [CustomizePermission]

    def get(self, request):
        user_id = request.user.id

        if user_id is None:
            return CustomResponse(
                general_message='User does not exist'
            ).get_failure_response()

        user = User.objects.filter(id=user_id).first()
        serializer = UserDetailsSerializer(user, many=False)

        return CustomResponse(response=serializer.data).get_success_response()


class ListAllVegetablesAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        vegetable = Vegetable.objects.all()
        serializer = ListAllVegetablesSerializer(vegetable, many=True)
        return CustomResponse(
            response=serializer.data
        ).get_success_response()


class UserFarmListAPI(APIView):
    authentication_classes = [CustomizePermission]

    def get(self, request):
        user_id = request.user.id

        if user_id is None:
            return CustomResponse(general_message='something went wrong').get_failure_response()

        user_farm_list = UserFarmLink.objects.filter(user=user_id).values(
            'id',
            farm_name=F('farm__name')
        )

        return CustomResponse(response=user_farm_list).get_success_response()