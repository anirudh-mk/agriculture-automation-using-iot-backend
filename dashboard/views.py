from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from utils.response import CustomResponse
from utils.permission import TokenGenerate

from .models import User, Farm, UserFarmLink


class CreateUserAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if User.objects.filter(username=username).exists():
            return CustomResponse(
                general_message="user name already exists"
            ).get_failure_response()

        if User.objects.filter(email=email).exists():
            return CustomResponse(
                general_message="email already registered"
            ).get_failure_response()

        if password != confirm_password:
            return CustomResponse(
                general_message="password and confirm password dose not match"
            ).get_failure_response()

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        user.save()

        return CustomResponse(
            general_message="user created successfully"
        ).get_success_response()


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
        name = request.data.get("name")
        description = request.data.get("description")
        user_id = request.data.get("user_id")

        user = User.objects.filter(id=user_id).first()

        farm = Farm.objects.create(
            name=name,
            description=description,
        )

        UserFarmLink.objects.create(
            farm=farm,
            user=user
        )

        return CustomResponse(
            general_message="farm created successfully"
        ).get_success_response()


class ListAllUsersAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        user = User.objects.all().values()
        return CustomResponse(response=user).get_success_response()