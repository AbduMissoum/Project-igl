from rest_framework.decorators import api_view,permission_classes
from rest_framework.parsers import JSONParser
from .models import Consultation
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .utils import (
    get_all_consultations, create_consultation,
    get_consultation_by_id, update_consultation,
    delete_consultation,get_consultation_resume_by_id,
    get_consultations_by_dpi,update_consultation_resume
    
)
from .docstrings import (consultation_list_schema,post_consultation_schema,consultation_detail_schema,put_consultation_schema,delete_consultation_schema,consultation_by_dpi_get_schema,consultation_resume_post_schema,consultation_resume_get_schema)

@consultation_list_schema()
@post_consultation_schema()
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def consultation_list(request):
    if request.method == 'GET':
        # Utilisation de la fonction utilitaire pour récupérer les consultations
        return get_all_consultations()

    elif request.method == 'POST':
           
            
        
            return create_consultation(request.user, request.data)

@put_consultation_schema()
@delete_consultation_schema()
@consultation_detail_schema()
@api_view(['GET', 'PUT', 'DELETE'])
def consultation_detail(request, pk):
    if request.method == 'GET':
        
        return get_consultation_by_id(pk)

    if request.method == 'PUT':
        return  update_consultation(pk, request.data)

    if request.method == 'DELETE':
        return delete_consultation(pk)
    
@consultation_by_dpi_get_schema()
@api_view(['GET'])
def consultation_by_dpi(request, pk):
    if request.method == 'GET':
        return get_consultations_by_dpi(pk)

@consultation_resume_get_schema()  
@consultation_resume_post_schema() 
@api_view(['GET', 'POST'])
def consultation_resume(request, pk):
    if request.method == 'GET':
        # Handle GET request to retrieve the resume
        return get_consultation_resume_by_id(pk)
    
    elif request.method == 'POST':
        try:
            # Debugging: Log incoming request data
            print("Received POST request data:", request.data)

            # Directly use `request.data` (no need for JSONParser as DRF handles this)
            data = request.data
            print("Parsed data:", data)

            # Call utility to update consultation resume
            return update_consultation_resume(pk, data)
        except Exception as e:
            print("Error during POST processing:", e)
            return Response({'error': 'Invalid request format or data'}, status=status.HTTP_400_BAD_REQUEST)
