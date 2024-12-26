from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



def soins_list_by_infirmier_schema():
    """
    Returns the OpenAPI schema for retrieving a list of soins for a specific infirmier.
    """
    patient_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "NSS": openapi.Schema(type=openapi.TYPE_STRING, example="1234567890"),
            "nom": openapi.Schema(type=openapi.TYPE_STRING, example="NIDAl"),
            "prenom": openapi.Schema(type=openapi.TYPE_STRING, example="Johnn"),
        }
    )

    soin_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            "patient": patient_schema,
            "description": openapi.Schema(type=openapi.TYPE_STRING, example="hello abdallah you are doing your best i love u"),
            "la_date": openapi.Schema(type=openapi.TYPE_STRING, example="1990-01-02"),
            "infirmier": openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of soins for the connected infirmier",
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of soins for the infirmier",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=soin_schema,
                ),
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred. Please try again later.'),
                    }
                ),
            ),
        }
    )
def soins_list_by_patient_id_schema():
    """
    Returns the OpenAPI schema for retrieving a list of soins for a specific patient.
    """
    infirmier_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, example='NIDAl1234567890'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, example='nlmll@esi.dz'),
        }
    )

    soin_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'description': openapi.Schema(type=openapi.TYPE_STRING, example="hello abdallah you are doing your best i love u"),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example="1990-01-02"),
            'patient': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
            'infirmier': infirmier_schema,
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of soins for a specific patient",
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of soins for the patient",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=soin_schema,
                ),
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred. Please try again later.'),
                    }
                ),
            ),
        }
    )