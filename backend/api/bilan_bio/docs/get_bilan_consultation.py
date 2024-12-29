from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def bilan_details():
    return swagger_auto_schema(
    method='GET',
    operation_summary="Get Bilan Biologique by Consultation ID",
    operation_description=(
        "Fetch the Bilan Biologique associated with a given consultation ID. "
        "Permissions: Accessible to the consultation's Medecin or Patient."
    ),
    manual_parameters=[
        openapi.Parameter(
            name="consultation_id",
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
            description="The ID of the consultation whose Bilan Biologique is to be retrieved.",
            required=True,
            example=123
        )
    ],
    responses={
        200: openapi.Response(
            description="Bilan Biologique retrieved successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'status': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="The result status of the request.",
                        example="success"
                    ),
                    'message': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        description="A list of parameters and their values for the Bilan.",
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'param_name': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Name of the parameter.",
                                    example="Glucose"
                                ),
                                'valeur': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Value of the parameter.",
                                    example="5.6"
                                ),
                                'unite': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Unit of the parameter value.",
                                    example="mmol/L"
                                ),
                                'valeur_reference': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Reference range for the parameter.",
                                    example="3.5-6.0 "
                                )
                            }
                        )
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred during the request.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Detailed error message.",
                        example="Consultation with ID 123 not found."
                    )
                }
            )
        )
    }
)