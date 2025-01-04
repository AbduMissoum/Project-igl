
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def get_bilan_schema():
    return swagger_auto_schema(
    method='GET',
    operation_description=(
        "Fetch a specific Bilan Radiologique by its ID and assign it to the authenticated radiologue. "
        "This operation ensures the radiologue becomes responsible for the Bilan."
    ),
    operation_summary="Fetch and assign a radiologue to a Bilan Radiologique record.",
    responses={
        200: openapi.Response(
            description="Successfully fetched and assigned the Bilan Radiologique.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Success message confirming the assignment.",
                        example="Bilan Radiologique assigned successfully."
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Invalid request or assignment error.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Error message explaining why the request failed.",
                        example="Invalid Bilan ID or assignment failed."
                    )
                }
            )
        ),
        403: openapi.Response(
            description="No permission to see bilan.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Error message indicating user has no permission.",
                        example="You do not have permission to perform this action."
                    )
                }
            )
        ),
        404: openapi.Response(
            description="Bilan Radiologique not found.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description="Error message indicating the Bilan was not found.",
                        example="Bilan Radiologique with the given ID does not exist."
                    )
                }
            )
        )
    }
)