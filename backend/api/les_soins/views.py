from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from .models import Soins
from .serializers import SoinsSerializer,SoinsSerializerDetail,SoinsWithPatientIdSerializer,SoinsWithInfirmierSerializer
from rest_framework.response import Response
from dpi.models import Patient
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def soins_list(request):
    if request.method == 'GET':
        soins = Soins.objects.all()
        serializer = SoinsSerializer(soins, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
      try: 
        soin = Soins(infirmier=request.user , 
                    description=request.data['description'],
                 patient=Patient.objects.get(NSS=request.data['NSS']),
                    la_date=request.data['la_date'])
        soin.save()
        serializer = SoinsSerializer(soin)
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      except Exception as e:
        print(e)
        return Response( {"error": "An unexpected error occurred. Please try again later."}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def soins_detail(request, pk):
 if request.method == 'GET':
    try : 
    
        soin = Soins.objects.get(pk=pk)
        serializer = SoinsSerializerDetail(soin)
        return Response(serializer.data)
    except Soins.DoesNotExist as e:
        print(e) 
        
        return Response( {"error": f"No soins with this id {pk}"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response( {"error": "An unexpected error occurred. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 if request.method  =='PATCH':
     try:
           serializer = SoinsSerializer(Soins.objects.get(pk=pk), data=request.data, partial=True)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)         
     except Exception as e:
        print(e)
        return Response( {"error": "An unexpected error occurred. Please try again later."}, status=status.HTTP_400_BAD_REQUEST)
    
 if request.method == 'DELETE':
    try:
        soin = Soins.objects.get(pk=pk)
        soin.delete()
        return Response( {"message": "Soins deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Soins.DoesNotExist as e:
        print(e) 
        
        return Response( {"error": f"No soins with this id {pk}"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response( {"error": "An unexpected error occurred. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def soins_list_by_patient_id(request,patient_id):
 try:
    soins  = Soins.objects.filter(patient=patient_id)
    serializer = SoinsWithPatientIdSerializer(soins, many=True)
    return Response(serializer.data)
 except Exception as e:
    print(e)
    return Response( {"error": "An unexpected error occurred. Please try again later."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])  
@permission_classes([IsAuthenticated])
def soins_with_infirmier(request):
    try:
        soins = Soins.objects.filter(infirmier=request.user)
        serializer = SoinsWithInfirmierSerializer(soins, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response( {"error": "An unexpected error occurred. Please try again later."}, status=status.HTTP_400_BAD_REQUEST)