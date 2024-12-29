from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def bilan_radio_update_schema():
    return swagger_auto_schema(
    operation_description="Update a radiological report (Bilan Radiologique) by adding or modifying the report content and uploading medical imaging examination files.",
    operation_summary="Update Radiological Report",
    manual_parameters=[
        openapi.Parameter(
            name='bilan_id',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
            description="ID of the radiological report to update.",
            required=True,
            example=123
        ),
        openapi.Parameter(
            name='compte_rendu',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_STRING,
            description="Content or description of the radiological report.",
            required=True,
            example="This is the updated report content."
        ),
        openapi.Parameter(
            name='examen_image',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_FILE,
            description="Medical imaging examination file to upload.",
            required=True
        )
    ],
    responses={
        200: openapi.Response(
            description="Successfully updated the radiological report.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(
                                type=openapi.TYPE_INTEGER, 
                                description="ID of the updated radiological report.",
                                example=123
                            ),
                            'examen_image': openapi.Schema(
                                type=openapi.TYPE_STRING, 
                                description="URL or path of the uploaded imaging file.",
                                example="https://example.com/uploads/examen_image_123.jpg"
                            )
                        }
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Bad Request - Invalid input data.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Error message detailing the issue with the request.",
                        example="Missing required fields: compte_rendu."
                    )
                }
            )
        ),
        403: openapi.Response(
            description="Forbidden - The user is not authorized to update this report.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Detailed error message indicating insufficient permissions.",
                        example="You do not have permission to update this radiological report."
                    )
                }
            )
        )
    },
)