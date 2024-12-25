from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Consultation
from django.http import JsonResponse
from .utils import (
    get_all_consultations, create_consultation,
    get_consultation_by_id, update_consultation,
    delete_consultation, get_consultations_by_date,
    create_consultations_by_date, get_consultations_by_dpi,
    create_consultations_by_dpi,create_consultation_by_medecin,
    get_consultations_by_medecin
)

@api_view(['GET', 'POST'])
def consultation_list(request):
    if request.method == 'GET':
        return get_all_consultations()

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        return create_consultation(data)


@api_view(['GET', 'PUT', 'DELETE'])
def consultation_detail(request, pk):
    if request.method == 'GET':
        return get_consultation_by_id(pk)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        consultation = Consultation.objects.get(pk=pk)  # Ensure the consultation exists
        return update_consultation(consultation, data)

    elif request.method == 'DELETE':
        consultation = Consultation.objects.get(pk=pk)  # Ensure the consultation exists
        return delete_consultation(consultation)


@api_view(['GET', 'POST'])
def consultation_by_date(request):
    if request.method == 'GET':
        consultation_date = request.GET.get('date', None)
        return get_consultations_by_date(consultation_date)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        return create_consultations_by_date(data)


@api_view(['GET', 'POST'])
def consultation_by_dpi(request, pk):
    if request.method == 'GET':
        return get_consultations_by_dpi(pk)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        return create_consultations_by_dpi(pk, data)

@api_view(['GET', 'POST'])
def consultation_by_medecin(request, medecin_id):
    if request.method == 'GET':
        return get_consultations_by_medecin(medecin_id)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        return create_consultation_by_medecin(medecin_id, data)
