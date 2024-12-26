from rest_framework.decorators import action
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def get_soin_list_schema():
    return  swagger_auto_schema(
    method='GET',
    operation_description="Retrieve a list of all soins (medical treatments)",
    responses={
        200: openapi.Response(
            description="Successfully retrieved list of soins",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                        'description': openapi.Schema(type=openapi.TYPE_STRING, example="hello abdallah you are doing your best i love u"),
                        'la_date': openapi.Schema(type=openapi.TYPE_STRING, example="1990-01-02"),
                        'patient': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                        'infirmier': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                    }
                ),
                examples={
                    'application/json': [
                        {
                            "id": 1,
                            "description": "hello abdallah you are doing your best i love u",
                            "la_date": "1990-01-02",
                            "patient": 5,
                            "infirmier": 5
                        },
                        {
                            "id": 2,
                            "description": "il doit avoir bouceau de medicament",
                            "la_date": "1990-01-02",
                            "patient": 5,
                            "infirmier": 5
                        },
                        {
                            "id": 3,
                            "description": "il doit avoir bouceau de medicament",
                            "la_date": "1990-01-02",
                            "patient": 5,
                            "infirmier": 5
                        }
                    ]
                }
            ),
        ),
        500: openapi.Response(
            description="Internal server error",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, example="Internal server error")
                }
            ),
            examples={
                'application/json': {
                    "error": "Internal server error"
                }
            }
        ),
    }
 )
    