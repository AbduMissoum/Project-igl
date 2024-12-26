from rest_framework.decorators import action
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def post_soin_schema():
    return swagger_auto_schema(
    method='POST',
    operation_description="Create a new soin (medical treatment)",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'description': openapi.Schema(type=openapi.TYPE_STRING, example="description"),
            'NSS': openapi.Schema(type=openapi.TYPE_STRING, example="NSS"),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example="2022-01-01"),
        }
    ),
    responses={
        201: openapi.Response(
            description="Successfully created soin",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=3),
                    'description': openapi.Schema(type=openapi.TYPE_STRING, example="il doit avoir bouceau de medicament"),
                    'la_date': openapi.Schema(type=openapi.TYPE_STRING, example="1990-01-02"),
                    'patient': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                    'infirmier': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                }
            ),
            examples={
                'application/json': {
                    "id": 3,
                    "description": "il doit avoir bouceau de medicament",
                    "la_date": "1990-01-02",
                    "patient": 5,
                    "infirmier": 5
                }
            }
        ),
        400: openapi.Response(
            description="Bad request",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, example=True),
                }
            ),
            examples={
                'application/json': {
                    "error": "An unexpected error occurred. Please try again later",
                }
            }
        ),
    }
)