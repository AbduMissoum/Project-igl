from django.http import JsonResponse
from .models import Consultation
from dpi.models import Dpi
from .serializers import ConsultationSerializer,ConsultationDetailSerializer
from rest_framework.parsers import JSONParser
from authentication.models import CustomUser,Etablisement
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from django.shortcuts import get_object_or_404


# Récupère toutes les consultations et retourne les données sérialisées
def get_all_consultations():
    consultations = Consultation.objects.all()
    serializer = ConsultationDetailSerializer(consultations, many=True)
    return Response(serializer.data)


# Crée une consultation à partir des données reçues
def create_consultation(user, data):
    try:
        # Récupérer l'établissement en fonction du nom
        etablisement = get_object_or_404(Etablisement, nom=data.get('etablisement'))
        dpi = get_object_or_404(Dpi, id=data.get('dpi'))

        # Créer l'objet Consultation
        consultation = Consultation(
            medecin=user,
            dpi=dpi,
            etablisement=etablisement,
            la_date=data.get('la_date')
        )
        consultation.save()

        # Sérialiser et retourner les données
        serializer = ConsultationSerializer(consultation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Etablisement.DoesNotExist:
        return Response({"error": "Etablissement not found."}, status=status.HTTP_400_BAD_REQUEST)
    except Dpi.DoesNotExist:
        return Response({"error": "Dpi not found."}, status=status.HTTP_400_BAD_REQUEST)
    except KeyError as e:
        return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({"error": "An unexpected error occurred. Please try again later."}, status=status.HTTP_400_BAD_REQUEST)

def get_consultation_by_id(pk):
    try:
        consultation = Consultation.objects.get(pk=pk)
        serializer = ConsultationDetailSerializer(consultation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Consultation.DoesNotExist:
        return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'error': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def update_consultation(pk, data):
    try:
        consultation = Consultation.objects.get(pk=pk)
        serializer = ConsultationDetailSerializer(consultation, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Consultation.DoesNotExist:
        return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'error': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def delete_consultation(pk):
    try:
        consultation = Consultation.objects.get(pk=pk)
        consultation.delete()
        return Response({'message': 'Consultation deleted successfully'}, status=status.HTTP_200_OK)
    except Consultation.DoesNotExist:
        return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'error': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def validate_date(date):
    """
    Valide le format de la date (YYYY-MM-DD).
    """
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return None  # Aucun problème
    except ValueError:
        return {'error': 'Invalid date format. Use YYYY-MM-DD.'}

def get_consultations_by_date(date):
    """
    Récupère les consultations pour une date donnée.
    """
    consultations = Consultation.objects.filter(la_date=date)
    if not consultations.exists():
        return {'message': 'No consultations found for this date'}, 404
    serializer = ConsultationSerializer(consultations, many=True)
    return serializer.data, 200


def get_consultations_by_dpi(pk):
    try:
        # Fetch the Dpi object by primary key
        dpi = Dpi.objects.get(pk=pk)
        
        # Filter consultations associated with the DPI
        consultations = Consultation.objects.filter(dpi=dpi)
        
        # Serialize the consultations using ConsultationDetailSerializer
        serializer = ConsultationDetailSerializer(consultations, many=True)
        
        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Dpi.DoesNotExist:
        # Handle case where DPI is not found
        return Response({'error': 'DPI not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Handle any unexpected errors
        print("Unexpected error:", str(e))
        return Response({'error': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_consultation_resume_by_id(pk):
    try:
        consultation = Consultation.objects.get(pk=pk)
        # Return only the `resume` field
        return Response({'resume': consultation.resume}, status=status.HTTP_200_OK)
    except Consultation.DoesNotExist:
        return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'error': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Utility function to update the resume of a consultation by ID
def update_consultation_resume(pk, data):
    try:
        # Ensure 'resume' field exists in the payload
        if 'resume' not in data:
            return Response({'error': "'resume' field is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the consultation object
        consultation = Consultation.objects.get(pk=pk)
        
        # Update the `resume` field
        consultation.resume = data['resume']
        consultation.save()
        
        # Return success response
        return Response({'message': 'Resume updated successfully', 'resume': consultation.resume}, status=status.HTTP_200_OK)
    except Consultation.DoesNotExist:
        return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print("Unexpected error:", e)
        return Response({'error': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

