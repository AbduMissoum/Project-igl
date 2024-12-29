from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .utils import bilan_rad
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsRadiologue,HasBilanAssignment,IsMedecin,IsPatient
from .models import BilanRadiologique
from .docs import demande_schema_radio,get_bilan_by_cons_schema,get_demande_schema,remplir_radio,voir_bilan_schema
# Create your views here.
@demande_schema_radio.demande_schema()
@api_view(['POST'])
@permission_classes([IsMedecin()])
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
@voir_bilan_schema.get_bilan_schema()
@api_view(['GET'])
@permission_classes([IsRadiologue()])
def get_bilan_radiologique(request:Request,bilan_id:int)->Response:
    rad_id = request.user.id
    if not rad_id:
        raise Exception("Error missing fields")
    result = bilan_rad.fetch_bilan(bilan_id,rad_id)
    if result['status']=='success':
        return Response({"message":result['message']},status=status.HTTP_200_OK)
    else:
        return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
@get_demande_schema.get_demandes_schema()
@api_view(['GET'])
@permission_classes([IsRadiologue()])
def get_demandes(request:Request)->Response:
    id = request.user.id
    result = bilan_rad.fetch_non_assigned(id)
    if result['status']=='success':
        return Response(result['message'],status=status.HTTP_200_OK)
    return Response(result['message'],status=status.HTTP_400_BAD_REQUEST)
class RemplirAPIView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    permission_classes = [IsAuthenticated,HasBilanAssignment]
    @remplir_radio.bilan_radio_update_schema()
    def patch(self,request:Request,bilan_id:int,format=None)->Response:
        self.check_object_permissions(self.request,BilanRadiologique.objects.get(id=bilan_id))
        # print(request.data)
        result = bilan_rad.remplissement_bilan(bilan_id,request.data)
        if result['status']=='success':
            return Response({"message":result['message']},status=status.HTTP_200_OK)
        else:
            return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
class ExamenImagerieByConsultationView(APIView):
    permission_classes = [IsPatient() | IsMedecin()]
    @get_bilan_by_cons_schema.bilan_detail()
    def get(self, request:Request, consultation_id:int)->Response:
        user_id = request.user.id
        result = bilan_rad.check_bilan(user_id,consultation_id)
        if result['status']=='success':
            return Response({"message":result['message']},status=status.HTTP_200_OK)
        else:
            return Response({"error":result['message']}, status=status.HTTP_400_BAD_REQUEST)
        