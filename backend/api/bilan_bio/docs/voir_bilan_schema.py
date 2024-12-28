from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def voir_bilan_schema():
    return swagger_auto_schema(
        method='GET',
        operation_description="Fetch and assign a laborantin to a specific Bilan Biologique by ID, and retrieve associated ParamValeur data.",
        operation_summary="Fetch and assign a laborantin to a specific Bilan Biologique record.",
        responses={
            200: openapi.Response(
                description="Successfully fetched and assigned Bilan Biologique",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT))
                    }
                )
            ),
            400: openapi.Response(
                description="Error occurred while fetching Bilan Biologique",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
                )
            ),
            404: openapi.Response(
                description="Bilan Biologique not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
                )
            )
        }
    )