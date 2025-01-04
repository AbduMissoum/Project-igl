from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from .utils import demand_bilan
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsMedecin,HasBilanAssignment,IsLaborantin,IsPatient
from .models import BilanBiologique

from .serializers import RemplirBilanRequestSerializer
from drf_yasg import openapi

from .docs import remplir_bilan_schema,voir_bilan_schema,notifications_schema,demande_schema,get_bilan_consultation




# Create your views here.
@demande_schema.demand_bio_schema()
@api_view(['POST'])
@permission_classes([IsMedecin()])
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

@permission_classes([HasBilanAssignment])
@remplir_bilan_schema.remplir_schema()
@api_view(['PUT'])
@permission_classes([HasBilanAssignment])
def remplir_bilan(request:Request,bilan_id:int)->Response:
    bilan = BilanBiologique.objects.get(id=bilan_id)
    permission = HasBilanAssignment()
    if not permission.has_object_permission(request,None,bilan):
        return Response({"message":"You don't have permissions to fill this bilan"},status=status.HTTP_403_FORBIDDEN)

    serializer = RemplirBilanRequestSerializer(data=request.data)
    if serializer.is_valid():
        param_valeurs_data = serializer.validated_data
        result = demand_bilan.remplissement_bilan(bilan_id, param_valeurs_data)

    if result['status']=='success':
        return Response({"message":"Bilan Satisfied"},status=status.HTTP_201_CREATED)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@voir_bilan_schema.voir_bilan_schema()
@api_view(['GET'])
@permission_classes([IsLaborantin()])
def get_bilan(request:Request,bilan_id:int)->Response:
    lab_id = request.user.id
    # print(f"Lab_id : {lab_id}",end="\n")
    result = demand_bilan.fetch_bilan(bilan_id,lab_id)
    if result['status']=='success':
        return Response(result['message'],status=status.HTTP_200_OK)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@notifications_schema.notificaions_schema()
@api_view(['GET'])
@permission_classes([IsLaborantin()])
def get_demandes(request:Request)->Response:
    id = request.user.id
    result = demand_bilan.fetch_non_assigned(id)
    # print(result)
    if result['status']=='success':
        return Response(result['message'],status=status.HTTP_200_OK)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@get_bilan_consultation.bilan_details() 
@api_view(['GET'])
def get_bilan_by_consultation_id(request:Request,consultation_id:int)->Response:

    user_id = request.user.id
    print("hhhhhhhhhhhhhhhhh")
    print(consultation_id)
    print(user_id)
    result = demand_bilan.check_bilan(consultation_id,user_id)

    if result['status']=='success':
        return Response(result['message'],status=status.HTTP_200_OK)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
