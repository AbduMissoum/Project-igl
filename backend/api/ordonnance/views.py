from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Medicament, Ordonnance, Traitement
from .serializers import MedicamentSerializer, OrdonnanceSerializer, TraitementSerializer
from .utils import (
    get_all_objects, get_object_or_404, create_object, update_object, delete_object, valider_ordonnance_util
)

from .docstrings import(ordonnance_list_schema,create_ordonnance_schema,ordonnance_detail_schema,valider_ordonnance_schema,update_ordonnance_schema,sup_ordonnance_schema,get_ordonnance_traitements_schema,post_ordonnance_traitements_schema,delete_traitement_schema,put_traitement_schema,traitement_detail_schema,post_traitement_schema,traitement_list_schema,post_medicament_schema,put_medicament_schema,delete_medicament_schema,medicament_detail_schema,medicament_list_schema)
from rest_framework.parsers import JSONParser

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

@ordonnance_list_schema()
@create_ordonnance_schema()
@api_view(['GET', 'POST'])
def ordonnance_list(request):
    if request.method == 'GET':
        return get_all_objects(Ordonnance, OrdonnanceSerializer)
    elif request.method == 'POST':
        return create_object(request, OrdonnanceSerializer)

@ordonnance_detail_schema()
@update_ordonnance_schema()
@sup_ordonnance_schema()
@api_view(['GET', 'PUT', 'DELETE'])
def ordonnance_detail(request, pk):
    ordonnance = get_object_or_404(Ordonnance, pk, 'Ordonnance not found')
    if isinstance(ordonnance, JsonResponse):  # Si c'est une erreur 404
        return ordonnance

    if request.method == 'GET':
        serializer = OrdonnanceSerializer(ordonnance)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        return update_object(request, ordonnance, OrdonnanceSerializer)
    elif request.method == 'DELETE':
        return delete_object(ordonnance)

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

@get_ordonnance_traitements_schema()
@post_ordonnance_traitements_schema()
@api_view(['GET', 'POST'])
def traitements_par_ordonnance(request, ordonnance_pk):
    ordonnance = get_object_or_404(Ordonnance, ordonnance_pk, 'Ordonnance not found')
    if isinstance(ordonnance, JsonResponse):  # Si c'est une erreur 404
        return ordonnance

    if request.method == 'GET':
        traitements = Traitement.objects.filter(ordonnance=ordonnance)
        serializer = TraitementSerializer(traitements, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if isinstance(data, list):
            for traitement in data:
                traitement['ordonnance'] = ordonnance.id
            serializer = TraitementSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201, safe=False)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({'error': 'Expected a list of treatments'}, status=400)

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

    serializer = OrdonnanceSerializer(ordonnance)
    return Response(serializer.data, status=status.HTTP_200_OK)

