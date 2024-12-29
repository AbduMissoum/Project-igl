from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def demande_schema():
    return swagger_auto_schema(
    method='POST',
    operation_description="Create a new Bilan Radiologique request for a consultation, with a specified type.",
    operation_summary="Create a new Bilan Radiologique request for a consultation.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'consultation_id': openapi.Schema(
                type=openapi.TYPE_INTEGER, 
                description="The ID of the consultation associated with the Bilan Radiologique request",
                example=123
            ),
            'type': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description="The type of the Bilan Radiologique request",
                example="IRM"
            )
        },
        required=['consultation_id', 'type']
    ),
    responses={
        201: openapi.Response(
            description="Successfully created a Bilan Radiologique request",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Success message indicating the Bilan was created successfully",
                        example="Bilan Radiologique request created successfully."
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while creating the Bilan Radiologique request",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Error message explaining why the request failed",
                        example="Invalid consultation ID or missing type field."
                    )
                }
            )
        )
    }
)