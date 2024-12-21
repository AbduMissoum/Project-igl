from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from dpi.utils import createPatient as util
from .serializers import PatientSerializer
import json
@api_view(["POST", "GET"])
def PatientList(request):
    if request.method == "GET":
        # Example: Return a message or list of patients (you can modify as needed)
        return Response({"message": "GET method not implemented yet"}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        # Call the createPatient utility function
        result = util.createPatient(data=request.data)
        if isinstance(result, dict) and "errors" in result:
            # Return validation errors if any
            return Response({"errors": result["errors"]}, status=status.HTTP_400_BAD_REQUEST)

        if result:
            
            # Return success response if a patient was created
         return Response({"message": "Patient created successfully", "patient_id": result["id"]}, status=status.HTTP_201_CREATED)

        # If creation failed for unknown reasons
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
