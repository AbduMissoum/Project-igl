from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .utils import bilan_rad
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.
@api_view(['POST'])
def demander_bilan_radiologique(request:Request)->Response:  
    consultation_id = request.data.get("consultation_id")
    type = request.data.get("type")
    if not consultation_id:
        raise Exception("Error missing fields")
    result = bilan_rad.faire_demande(consultation_id,type)
    if result['status']=='success':
        return Response({"message":"Demand successfuly created"},status=status.HTTP_201_CREATED)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_bilan_radiologique(request:Request,bilan_id:int)->Response:
    rad_id = request.query_params.get("rad_id")
    if not rad_id:
        raise Exception("Error missing fields")
    result = bilan_rad.fetch_bilan(bilan_id,rad_id)
    if result['status']=='success':
        return Response({"message":result['message']},status=status.HTTP_200_OK)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_demandes(request:Request)->Response:
    result = bilan_rad.fetch_non_assigned()
    if result['status']=='success':
        return Response(result['message'],status=status.HTTP_200_OK)
    return Response(result['message'],status=status.HTTP_400_BAD_REQUEST)
class RemplirAPIView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    def patch(sef,request:Request,bilan_id:int,format=None)->Response:
        print(request.data)
        result = bilan_rad.remplissement_bilan(bilan_id,request.data)
        if result['status']=='success':
            return Response({"message":result['message']},status=status.HTTP_200_OK)
        else:
            return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)