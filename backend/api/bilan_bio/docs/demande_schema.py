from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def demand_bio_schema():
    return swagger_auto_schema(
    method='POST',
    operation_description=(
        "Create a new Bilan Biologique request associated with a specific consultation. "
        "Provide a list of test names to be included in the Bilan."
    ),
    operation_summary="Create a new Bilan Biologique request for a consultation.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'tests': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING),
                description="List of test names for the Bilan request.",
                example=["Complete Blood Count", "Liver Function Test", "Thyroid Profile"]
            ),
            'consultation_id': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="The ID of the consultation associated with the Bilan request.",
                example=456
            )
        },
        required=['tests', 'consultation_id']
    ),
    responses={
        201: openapi.Response(
            description="Successfully created a Bilan Biologique request.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Success message indicating the Bilan was created successfully.",
                        example="Bilan Biologique request created successfully."
                    ),
                    'bilan_id': openapi.Schema(
                        type=openapi.TYPE_INTEGER, 
                        description="The ID of the newly created Bilan.",
                        example=789
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while creating the Bilan Biologique request.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Error message explaining why the request failed.",
                        example="Invalid consultation ID or empty test list."
                    )
                }
            )
        )
    }
)