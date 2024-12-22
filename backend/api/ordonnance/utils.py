from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist


def get_all_objects(model, serializer_class):
    """Récupère tous les objets pour un modèle donné."""
    objects = model.objects.all()
    serializer = serializer_class(objects, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_object_or_404(model, pk, error_message):
    """Récupère un objet ou renvoie une erreur 404."""
    try:
        return model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({'error': error_message}, status=404)


def create_object(request, serializer_class):
    """Crée un objet pour un modèle donné."""
    data = JSONParser().parse(request)
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


def update_object(request, instance, serializer_class):
    """Met à jour un objet existant."""
    data = JSONParser().parse(request)
    serializer = serializer_class(instance, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


def delete_object(instance):
    """Supprime un objet existant."""
    instance.delete()
    return JsonResponse({'message': 'Deleted successfully'}, status=204)
