from django.urls import path
from . import views

urlpatterns = [
    path('user/register/', views.CreateUserAPI.as_view()),
    path('user/login/', views.UserLoginAPI.as_view()),
    path('farm/create/', views.FarmCreateAPI.as_view()),
    path('user/list/', views.ListAllUsersAPI.as_view()),
    path('user/details/', views.UserDetailsAPI.as_view()),
]
