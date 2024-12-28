from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def notificaions_schema():
    return swagger_auto_schema(
    method='GET',
    operation_description="Fetch all non-assigned Bilan Biologique records for a laborantin, filtered by establishment and satisfaction status.",
    operation_summary="Fetch non-assigned Bilan Biologique records for a laborantin.",
    responses={
        200: openapi.Response(
            description="Successfully fetched non-assigned Bilans",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT))
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while fetching non-assigned Bilans",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        ),
        404: openapi.Response(
            description="No non-assigned Bilans found for the laborantin",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        )
    }
)