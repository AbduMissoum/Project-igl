from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def notificaions_schema():
    return swagger_auto_schema(
    method='GET',
    operation_description=(
        "Retrieve all non-assigned Bilan Biologique records available for the authenticated laborantin. "
        "The records are filtered by the laborantin's establishment and satisfaction status."
    ),
    operation_summary="Fetch non-assigned Bilan Biologique records for a laborantin.",
    responses={
        200: openapi.Response(
            description="Successfully fetched non-assigned Bilan Biologique records.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="A success message indicating the records were fetched.",
                        example="Non-assigned Bilan Biologique records retrieved successfully."
                    ),
                    'bilans': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        description="List of non-assigned Bilan Biologique records.",
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'bilan_id': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description="Unique ID of the Bilan Biologique record.",
                                    example=101
                                ),
                                'consultation_id': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description="ID of the associated consultation.",
                                    example=456
                                ),
                                'tests': openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    description="List of test names in the Bilan Biologique record.",
                                    example=["Complete Blood Count", "Liver Function Test"]
                                ),
                                'status': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Current status of the Bilan Biologique.",
                                    example="Pending"
                                ),
                                'establishment_id': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description="ID of the establishment associated with the Bilan.",
                                    example=789
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
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error message explaining why the request failed.",
                        example="Invalid filter parameters."
                    )
                }
            )
        ),
        404: openapi.Response(
            description="The requested resource was not found",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'status': openapi.Schema(type=openapi.TYPE_STRING),
                    'message': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
    }
)