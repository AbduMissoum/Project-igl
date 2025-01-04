from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from dpi.utils import createPatient as createPatient,searchDpi as search,mailService
from .serializers import PatientSerializer,PatientSerializerWithId,MedcinListSerializer
import json
from .models import Patient
from authentication.models import CustomUser
from .docstrings.docPatient import patient_detail_schema,patient_list_by_nss_schema,create_patient_schema,medecin_list_schema

from rest_framework.permissions import IsAuthenticated,AllowAny







@create_patient_schema()
@patient_list_by_nss_schema() 
@api_view(["POST", "GET"])
def PatientList(request):
    if request.method == "GET":
        res = search.searchDpiNSS(request=request)
        if "error" in  res : 
          return Response(res,status=status.HTTP_400_BAD_REQUEST)
        elif  res or len(res)>=0: 
          return Response(res)
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    elif request.method == "POST":
        # Call the createPatient utility function
        result = createPatient.createPatient(data=request.data)
        if isinstance(result, dict) and "errors" in result:
            # Return validation errors if any
            return Response({"errors": result["errors"]}, status=status.HTTP_400_BAD_REQUEST)

        if result:
         mailService.sendMail(email=result["email"],
                               username=result["username"],
                               password=result["password"])
            
            # Return success response if a patient was created
         return Response({"message": "Patient created successfully", "patient": result["patient"]}, status=status.HTTP_201_CREATED)

        # If creation failed for unknown reasons
      
  
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@patient_detail_schema()
@api_view(["GET","DELETE"])


def PatientDetail(request, id):
  if(request.method == "GET"):
    try:
        # Fetch the patient object by primary key (id)
        patient = Patient.objects.get(id=id)
        serializer = PatientSerializerWithId(patient)
      
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Patient.DoesNotExist:
        # Return a 404 response if the patient does not exist
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        # Log the exception for debugging (optional)
      
        print(e)
        # Return a 500 response for any unexpected errors
        return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@medecin_list_schema()
@api_view(["GET"])      
def MedcinList(request): 
   try: 
    medcinList = CustomUser.objects.filter(role="medecin").values("id","username","email")
    res =  MedcinListSerializer(medcinList,many=True)
    return Response(res.data)
   except Exception as e:
    return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@permission_classes([AllowAny])
@api_view(["GET"])
def creer_role(req):
  try:
    # user =  CustomUser.objects.create_user(username="patient",
    #                                        email="patient@esi.dz",
    #                                         password="patient",
    #                                         role="patient")
    
    # user =  CustomUser.objects.create_user(username="admin",
    #                                        email="admin@esi.dz",
    #                                         password="admine",
    #                                         role="admin")
    user =  CustomUser.objects.create_user(username="infirmier",
                                           email="infirmier@esi.dz",
                                            password="infirmier",
                                            role="infirmier")
    user =  CustomUser.objects.create_user(username="radiologue",
                                           email="radiologue@esi.dz",
                                            password="radiologue",
                                            role="radiologue")
    user =  CustomUser.objects.create_user(username="laborantin",
                                           email="laborantin@esi.dz",
                                            password="laborantin",
                                            role="laborantin")
    user =  CustomUser.objects.create_user(username="medecin",
                                           email="medecin@esi.dz",
                                            password="medecin",
                                            role="medecin")
    return Response({"message": "Role created successfully"}, status=status.HTTP_201_CREATED)
  except Exception as e:
    return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)