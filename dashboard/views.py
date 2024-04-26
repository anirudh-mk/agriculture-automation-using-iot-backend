import uuid

from django.db.models import Q, F, Prefetch
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from utils.response import CustomResponse
from utils.permission import TokenGenerate, CustomizePermission

from .models import User, Farm, UserFarmLink, Vegetable, FarmVegetableLink, FarmNPKLink
from .serializer import (UserCreateSerializer,
                         FarmCreateSerializer,
                         ListAllUsersSerializer,
                         UserDetailsSerializer,
                         ListAllVegetablesSerializer,
                         UserFarmListSerializer,
                         VegetableCreateSerializer,
                         FarmVegetableCreateSerializer)


from django.db.models import Prefetch

from django.db.models import Prefetch


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
        print(user)
        if user:
            auth = TokenGenerate().generate(user)
            return CustomResponse(
                general_message="successfully login",
                response=[auth, {"is_admin": user.is_admin}],
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
            farm = serializer.save()
            return CustomResponse(
                general_message='Farm created successfully',
                response=farm.id
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
    permission_classes = (AllowAny,)

    def post(self, request):
        user_id = request.data.get('user_id')
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
            return CustomResponse(
                general_message='something went wrong'
            ).get_failure_response()

        user_farm_link = UserFarmLink.objects.filter(user=user_id).all()

        serializer = UserFarmListSerializer(user_farm_link, many=True)

        return CustomResponse(response=serializer.data).get_success_response()


class VegetableCreateAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = VegetableCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(
                general_message='Vegetable created successfully'
            ).get_success_response()

        return CustomResponse(
            response=serializer.errors
        ).get_failure_response()


class UserBasicDetails(APIView):
    authentication_classes = [CustomizePermission]

    def get(self, request):
        user_id = request.user.id

        user = User.objects.filter(id=user_id).values()

        return CustomResponse(response=user).get_success_response()


class VegetableDetails(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        vegetable_id = request.data.get('vegetable_id')

        vegetable = Vegetable.objects.filter(id=vegetable_id).values()

        return CustomResponse(response=vegetable).get_success_response()


class FarmVegetableCreate(APIView):
    authentication_classes = [CustomizePermission]

    def post(self, request):

        user_farm_link = request.data.get('farm')
        vegetable = request.data.get('vegetable')

        farm_obj = UserFarmLink.objects.filter(id=user_farm_link).first()
        vegetable_obj = Vegetable.objects.filter(id=vegetable).first()

        farm_vegetable_link = FarmVegetableLink.objects.create(
            id=uuid.uuid4(),
            farm=farm_obj.farm,
            vegetable=vegetable_obj
        )

        return CustomResponse(
            response=farm_vegetable_link.id
        ).get_failure_response()


class NPKSend(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, farm_id):
        farm_vegetable_link = FarmVegetableLink.objects.filter(id=farm_id, is_completed=0).first()
        vegetable = Vegetable.objects.filter(id=farm_vegetable_link).values('n', 'p', 'k', 'time_required')


class NPKPost(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, farm_id):

        n = request.GET.get('n')
        p = request.GET.get('p')
        k = request.GET.get('k')

        farm = Farm.objects.filter(id=farm_id).first()

        FarmNPKLink.objects.create(
            id=uuid.uuid4(),
            n=n,
            p=p,
            k=k,
            farm=farm
        )

        return CustomResponse(
            general_message='success'
        ).get_failure_response()

class FarmStatistics(APIView):
    authentication_classes = [CustomizePermission]

    def get(self, request):
        user_id = request.user.id

        # Fetch UserFarmLink objects for the user
        user_farm_links = UserFarmLink.objects.filter(user_id=user_id, is_completed=False)

        # Prefetch related FarmVegetableLink objects and select related Vegetable objects
        user_farm_links = user_farm_links.prefetch_related(
            Prefetch('farm__farm_vegetable_link_farm', queryset=FarmVegetableLink.objects.select_related('vegetable'))
        )

        # Extract vegetable names and their creation dates from the prefetched data
        vegetable_info = []
        for link in user_farm_links:
            for farm_vegetable_link in link.farm.farm_vegetable_link_farm.all():
                vegetable_name = farm_vegetable_link.vegetable.name
                creation_date = farm_vegetable_link.created_at.strftime('%Y-%m-%d')
                vegetable_info.append({'name': vegetable_name, 'created_at': creation_date})

        return CustomResponse(
            response=vegetable_info
        ).get_success_response()


class NPKReadings(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, farm_id):
        farm_npk_link = FarmNPKLink.objects.filter(farm=farm_id).all().values()
        return CustomResponse(response=farm_npk_link).get_success_response()
