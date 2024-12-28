from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Consultation
from django.http import JsonResponse
from rest_framework.response import Response

from .utils import (
    get_all_consultations, create_consultation,
    get_consultation_by_id, update_consultation,
    delete_consultation, get_consultations_by_date,

    get_consultations_by_dpi,validate_date,

    create_consultations_by_dpi,create_consultation_by_medecin,
    get_consultations_by_medecin
)
from .docstrings import (consultation_list_schema,post_consultation_schema,consultation_detail_schema,put_consultation_schema,delete_consultation_schema,consultation_by_medecin_get_schema,consultation_by_medecin_post_schema,consultation_by_dpi_get_schema,consultation_by_dpi_post_schema,consultation_by_date_get_schema)

@consultation_list_schema()
@post_consultation_schema()
@api_view(['GET', 'POST'])
def consultation_list(request):
    if request.method == 'GET':
        return get_all_consultations()

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        return create_consultation(data)

@put_consultation_schema()
@delete_consultation_schema()
@consultation_detail_schema()
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

@consultation_by_date_get_schema()
@api_view(['GET'])
def consultation_by_date(request, date):
    """
    Get consultations by date.
    """
    # Valider la date
    validation_error = validate_date(date)
    if validation_error:
        return Response(validation_error, status=400)

    # Obtenir les consultations
    data, status_code = get_consultations_by_date(date)
    return Response(data, status=status_code)
    
@consultation_by_dpi_get_schema()
@consultation_by_dpi_post_schema()
@api_view(['GET', 'POST'])
def consultation_by_dpi(request, pk):
    if request.method == 'GET':
        return get_consultations_by_dpi(pk)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        return create_consultations_by_dpi(pk, data)

@consultation_by_medecin_post_schema()
@consultation_by_medecin_get_schema()
@api_view(['GET', 'POST'])
def consultation_by_medecin(request, medecin_id):
    if request.method == 'GET':
        return get_consultations_by_medecin(medecin_id)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        return create_consultation_by_medecin(medecin_id, data)




