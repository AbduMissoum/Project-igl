from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.middleware.csrf import get_token
import json

from .models import CustomUser
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view
from rest_framework import status
from django.middleware.csrf import get_token 
from dpi.serializers import PatientSerializer
# Create your views here.
from django.core.mail import send_mail
from .utils import content

#docs 
from .docstrings.docAuth import login_schema,logout_schema
@csrf_exempt
@login_schema()
@api_view(["POST"])

def logUser(req):
        
    if(req.user.is_authenticated):
            print(req.user.id)
            print("hhhhhhhh")
     
        
            return JsonResponse({"mesage":"User already authenticated","role":req.user.role,"id":req.user.id})
    else : 
      try :  
        print(req.COOKIES)  
        username = req.data['username']
        password = req.data['password']
        
        
 
        
        user = authenticate(username=username,password=password)
        if(user) : 
            login(req,user)
            return JsonResponse({"mesage":"User authenticated","role":user.role,"id":user.id})
        else :  
            return JsonResponse({"message":"invalid credentials"},status=status.HTTP_404_NOT_FOUND)
      except KeyError as e: 
        return JsonResponse({"message":f"key is missing {e}"},status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@logout_schema()
@api_view(["POST"])
def logoutUser(req):
        
        logout(req)
        return JsonResponse({"message":"User logged out"})
