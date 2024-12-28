from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def get_demandes_schema():
    """
    Returns a swagger_auto_schema decorator for the get_demandes endpoint
    """
    return swagger_auto_schema(
    method='GET',
    operation_description="Fetch non-assigned Bilan Radiologique for the authenticated radiologue user.",
    operation_summary="Fetch all non-assigned Bilan Radiologique records for a specific radiologue.",
    responses={
        200: openapi.Response(
            description="Successfully fetched non-assigned Bilans",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'status': openapi.Schema(type=openapi.TYPE_STRING),
                    'message': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT))
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while fetching non-assigned Bilans",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'status': openapi.Schema(type=openapi.TYPE_STRING), 'message': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        )
    }
)