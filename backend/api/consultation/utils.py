from django.http import JsonResponse
from .models import Consultation
from dpi.models import Dpi
from .serializers import ConsultationSerializer
from rest_framework.parsers import JSONParser


def get_all_consultations():
    consultations = Consultation.objects.all()
    serializer = ConsultationSerializer(consultations, many=True)
    return JsonResponse(serializer.data, safe=False)


def create_consultation(data):
    serializer = ConsultationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


def get_consultation_by_id(pk):
    try:
        consultation = Consultation.objects.get(pk=pk)
        serializer = ConsultationSerializer(consultation)
        return JsonResponse(serializer.data, safe=False)
    except Consultation.DoesNotExist:
        return JsonResponse({'error': 'Consultation not found'}, status=404)


def update_consultation(consultation, data):
    serializer = ConsultationSerializer(consultation, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


def delete_consultation(consultation):
    consultation.delete()
    return JsonResponse({'message': 'Consultation deleted successfully'}, status=204)


def get_consultations_by_date(consultation_date=None):
    if consultation_date:
        consultations = Consultation.objects.filter(la_date=consultation_date)
    else:
        consultations = Consultation.objects.all()
    serializer = ConsultationSerializer(consultations, many=True)
    return JsonResponse(serializer.data, safe=False)


def create_consultations_by_date(data):
    if isinstance(data, list):
        serializer = ConsultationSerializer(data=data, many=True)
    else:
        serializer = ConsultationSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201, safe=False)
    return JsonResponse(serializer.errors, status=400)


def get_consultations_by_dpi(pk):
    try:
        dpi = Dpi.objects.get(pk=pk)
        consultations = Consultation.objects.filter(dpi=dpi)
        serializer = ConsultationSerializer(consultations, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Dpi.DoesNotExist:
        return JsonResponse({'error': 'DPI not found'}, status=404)


def create_consultations_by_dpi(pk, data):
    if isinstance(data, list):
        for item in data:
            item['dpi'] = pk
        serializer = ConsultationSerializer(data=data, many=True)
    else:
        data['dpi'] = pk
        serializer = ConsultationSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201, safe=False)
    return JsonResponse(serializer.errors, status=400)
