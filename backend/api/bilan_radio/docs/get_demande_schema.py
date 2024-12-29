from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def get_demandes_schema():
    """
    Returns a swagger_auto_schema decorator for the get_demandes endpoint
    """
    return swagger_auto_schema(
    method='GET',
    operation_description="Fetch non-assigned Bilan Radiologique records for the authenticated radiologue user. This endpoint retrieves all Bilans that have not yet been assigned to any radiologue.",
    operation_summary="Fetch all non-assigned Bilan Radiologique records.",
    responses={
        200: openapi.Response(
            description="Successfully fetched non-assigned Bilans.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'status': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="The status of the operation, typically 'success'.",
                        example="success"
                    ),
                    'message': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        description="A list of non-assigned Bilans.",
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'bilan_id': openapi.Schema(
                                    type=openapi.TYPE_INTEGER, 
                                    description="Unique identifier of the Bilan.",
                                    example=101
                                ),
                                'consultation_id': openapi.Schema(
                                    type=openapi.TYPE_INTEGER, 
                                    description="The ID of the consultation associated with the Bilan.",
                                    example=1234
                                ),
                                'type': openapi.Schema(
                                    type=openapi.TYPE_STRING, 
                                    description="The type of the Bilan Radiologique.",
                                    example="Radiological Examination"
                                ),
                                'created_at': openapi.Schema(
                                    type=openapi.TYPE_STRING, 
                                    format="date-time",
                                    description="The date and time when the Bilan was created.",
                                    example="2023-12-01T14:30:00Z"
                                )
                            }
                        )
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while fetching non-assigned Bilans.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'status': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="The status of the operation, typically 'error'.",
                        example="error"
                    ),
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Details about the error that occurred.",
                        example="No non-assigned Bilans found for the authenticated radiologue."
                    )
                }
            )
        )
    }
)