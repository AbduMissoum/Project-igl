
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def get_bilan_schema():
    return swagger_auto_schema(
    method='GET',
    operation_description="Fetch and assign a radiologue to a specific Bilan Radiologique by ID.",
    operation_summary="Fetch and assign a radiologue to a specific Bilan Radiologique record.",
    responses={
        200: openapi.Response(
            description="Successfully fetched and assigned Bilan Radiologique",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while fetching Bilan Radiologique",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        ),
        404: openapi.Response(
            description="Bilan Radiologique not found",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        )
    }
)