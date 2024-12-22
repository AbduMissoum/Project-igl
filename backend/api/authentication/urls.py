from django.urls import path
from .views import logUser,logoutUser
urlpatterns=[
    path('login/',logUser),
    path('logout/',logoutUser),   
]