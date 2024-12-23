from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .utils import demand_bilan
from rest_framework import status
#from .models import BilanBiologique

# Create your views here.
@api_view(['POST'])
def demander_bilan(request:Request)->Response:
    test_names = request.data.get("tests", [])  # List of test names
    consultation_id = request.data.get("consultation_id")
    if not test_names or not consultation_id:
        raise Exception("Error missing fields")
    result = demand_bilan.faire_demande(test_names,consultation_id)
    if result['status']=='success':
        return Response({"message":"Demand successfuly created"},status=status.HTTP_201_CREATED)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def remplir_bilan(request:Request,bilan_id:int)->Response:
    result = demand_bilan.remplissement_bilan(bilan_id,request.data)
    if result['status']=='success':
        return Response({"message":"Bilan Satisfied"},status=status.HTTP_201_CREATED)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_bilan(request:Request,bilan_id:int)->Response:
    lab_id = request.query_params.get("lab_id")
    # print(f"Lab_id : {lab_id}",end="\n")
    result = demand_bilan.fetch_bilan(bilan_id,lab_id)
    if result['status']=='success':
        return Response(result['message'],status=status.HTTP_200_OK)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_demandes(request:Request)->Response:
    result = demand_bilan.fetch_non_assigned()
    # print(result)
    if result['status']=='success':
        return Response(result['message'],status=status.HTTP_200_OK)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST) 
