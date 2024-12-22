from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from dpi.utils import createPatient as createPatient,searchDpi as search
from .serializers import PatientSerializer,PatientSerializerWithId
import json
from .models import Patient
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
            
            # Return success response if a patient was created
         return Response({"message": "Patient created successfully", "patient_id": result["id"]}, status=status.HTTP_201_CREATED)

        # If creation failed for unknown reasons
      
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET","PATCH","DELETE"])


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