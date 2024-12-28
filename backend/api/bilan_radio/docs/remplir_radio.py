from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def bilan_radio_update_schema():
    return swagger_auto_schema(
    operation_description="Update a radiological report (Bilan Radiologique) with examination images",
    operation_summary="Update Radiological Report",
    manual_parameters=[
        openapi.Parameter(
            name='bilan_id',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
            description='ID of the radiological report to update',
            required=True
        ),
        openapi.Parameter(
            name='compte_rendu',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_STRING,
            description='Report content/description',
            required=True
        ),
        openapi.Parameter(
            name='examen_image',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_FILE,
            description='Medical imaging examination file',
            required=True
        )
    ],
    responses={
        200: openapi.Response(
            description='Success',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'examen_image': openapi.Schema(type=openapi.TYPE_STRING)
                        }
                    )
                }
            )
        ),
        400: openapi.Response(
            description='Bad Request',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        403: openapi.Response(
            description='Forbidden',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        )
    },
)