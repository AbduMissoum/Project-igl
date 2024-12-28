from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def demand_bio_schema():
    return swagger_auto_schema(
    method='POST',
    operation_description="Create a new Bilan Biologique request for a consultation, with a list of test names.",
    operation_summary="Create a new Bilan Biologique request for a consultation.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'tests': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING), description="List of test names for the Bilan request"),
            'consultation_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="The ID of the consultation associated with the Bilan request")
        },
        required=['tests', 'consultation_id']
    ),
    responses={
        201: openapi.Response(
            description="Successfully created a Bilan Biologique request",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description="Success message indicating the Bilan was created successfully")
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while creating the Bilan Biologique request",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'error': openapi.Schema(type=openapi.TYPE_STRING, description="Error message explaining why the request failed")}
            )
        )
    }
)