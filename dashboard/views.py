from rest_framework.views import APIView
from .models import User
from utils.response import CustomResponse
from rest_framework.permissions import AllowAny


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
