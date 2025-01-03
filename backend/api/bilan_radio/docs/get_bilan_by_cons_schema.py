from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def bilan_detail():
    return swagger_auto_schema(
    operation_description="Retrieve the medical imaging examination (ExamenImagerieMedicale) for a given consultation ID.",
    manual_parameters=[
        openapi.Parameter(
            'consultation_id',
            openapi.IN_PATH,
            description="ID of the consultation to retrieve the associated medical imaging examination.",
            type=openapi.TYPE_INTEGER,
            required=True
        )
    ],
    responses={
        200: openapi.Response(
            description="Success response with examen data",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(
                        type=openapi.TYPE_INTEGER, 
                        description="ID of the examen",
                        example=1
                    ),
                    "bilan": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "id": openapi.Schema(
                                type=openapi.TYPE_INTEGER, 
                                description="ID of the bilan",
                                example=2
                            ),
                            "compte_rendu": openapi.Schema(
                                type=openapi.TYPE_STRING, 
                                description="Report details",
                                example="Sample report"
                            ),
                        }
                    ),
                    "examen_image": openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Image data",
                        example="Path to the image."
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Error response when no bilan is found for the consultation.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Error message",
                        example="No bilan found for the given consultation_id"
                    )
                }
            )
        ),403: openapi.Response(
            description="Forbiden - User does not have permission.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="No permission",
                        example="You don't have permissions to perform this action."
                    )
                }
            )
        )
    }
)