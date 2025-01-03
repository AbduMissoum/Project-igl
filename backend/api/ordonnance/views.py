from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Medicament, Ordonnance, Traitement
from .serializers import MedicamentSerializer, OrdonnanceSerializer, TraitementSerializer
from .utils import (
    get_all_objects, get_object_or_404, create_object, update_object, delete_object, valider_ordonnance_util
)
from .docstrings import(ordonnance_list_schema,create_ordonnance_schema,valider_ordonnance_schema,ordonnance_detail_schema,update_ordonnance_schema,sup_ordonnance_schema,delete_traitement_schema,put_traitement_schema,traitement_detail_schema,post_traitement_schema,traitement_list_schema,post_medicament_schema,put_medicament_schema,delete_medicament_schema,medicament_detail_schema,medicament_list_schema,ordonnances_by_consultation_schema)
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from consultation.models import Consultation

@medicament_list_schema()
@post_medicament_schema()
@api_view(['GET', 'POST'])
def medicament_list(request):
    if request.method == 'GET':
        return get_all_objects(Medicament, MedicamentSerializer)
    elif request.method == 'POST':
        return create_object(request, MedicamentSerializer)

@put_medicament_schema()
@delete_medicament_schema()
@medicament_detail_schema()
@api_view(['GET', 'PUT', 'DELETE'])
def medicament_detail(request, pk):
    medicament = get_object_or_404(Medicament, pk, 'Medicament not found')
    if isinstance(medicament, JsonResponse):  # Si c'est une erreur 404
        return medicament

    if request.method == 'GET':
        serializer = MedicamentSerializer(medicament)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        return update_object(request, medicament, MedicamentSerializer)
    elif request.method == 'DELETE':
        return delete_object(medicament)

@create_ordonnance_schema()
@api_view(['POST'])
def ordonnance_create(request):
    """
    API endpoint to create an Ordonnance with a list of Traitements.
    """
    if request.method == 'POST':
        serializer = OrdonnanceSerializer(data=request.data)
        if serializer.is_valid():
            ordonnance = serializer.save()
            return Response(
                {"message": "Ordonnance created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@ordonnance_detail_schema()
@update_ordonnance_schema()
@sup_ordonnance_schema()
@api_view(['GET', 'PUT', 'DELETE'])
def ordonnance_detail(request, pk):
    ordonnance = get_object_or_404(Ordonnance, pk=pk)
    
    if request.method == 'GET':
        # Si la méthode est GET, renvoyer les détails de l'ordonnance
        serializer = OrdonnanceSerializer(ordonnance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Si la méthode est PUT, mettre à jour l'ordonnance existante
        serializer = OrdonnanceSerializer(ordonnance, data=request.data)
        if serializer.is_valid():
            # Si les données sont valides, enregistrer les modifications
            serializer.save()
            # Retourner une réponse avec un message de succès
            return Response({
                'message': 'Ordonnance updated successfully!',
                'data': serializer.data
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si la méthode est DELETE, supprimer l'ordonnance
        ordonnance.delete()
        return Response({'message': 'Consultation deleted successfully'}, status=status.HTTP_200_OK)

@traitement_list_schema()
@post_traitement_schema()
@api_view(['GET', 'POST'])
def traitement_list(request):
    if request.method == 'GET':
        return get_all_objects(Traitement, TraitementSerializer)
    elif request.method == 'POST':
        return create_object(request, TraitementSerializer)

@traitement_detail_schema()
@put_traitement_schema()
@delete_traitement_schema()
@api_view(['GET', 'PUT', 'DELETE'])
def traitement_detail(request, pk):
    traitement = get_object_or_404(Traitement, pk, 'Traitement not found')
    if isinstance(traitement, JsonResponse):  # Si c'est une erreur 404
        return traitement

    if request.method == 'GET':
        serializer = TraitementSerializer(traitement)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        return update_object(request, traitement, TraitementSerializer)
    elif request.method == 'DELETE':
        return delete_object(traitement)


@valider_ordonnance_schema()
@api_view(['POST'])
def valider_ordonnance(request, pk):
    """
    Vue pour valider une ordonnance en utilisant la fonction utilitaire.
    """
    try:
        ordonnance = valider_ordonnance_util(pk)
    except ValueError as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"error": "Ordonnance not found"}, status=status.HTTP_404_NOT_FOUND)

    # Sérialiser l'ordonnance validée pour la réponse
    serializer = OrdonnanceSerializer(ordonnance)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@ordonnances_by_consultation_schema()
@api_view(['GET'])
def ordonnances_by_consultation(request, consultation_id):
    """
    Get all ordonnances for a specific consultation.
    """
    try:
        consultation = Consultation.objects.get(id=consultation_id)
    except Consultation.DoesNotExist:
        return Response({"message": "Consultation not found"}, status=status.HTTP_404_NOT_FOUND)

    # Filtrer les ordonnances associées à la consultation
    ordonnances = Ordonnance.objects.filter(consultation=consultation)

    # Sérialiser les ordonnances et renvoyer la réponse
    serializer = OrdonnanceSerializer(ordonnances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
