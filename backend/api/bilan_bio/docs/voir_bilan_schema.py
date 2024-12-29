from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def voir_bilan_schema():
    return swagger_auto_schema(
    method='GET',
    operation_description=(
        "Retrieve and assign a laborantin to a specific Bilan Biologique by ID. "
        "The response includes associated ParamValeur data and confirms the successful assignment."
    ),
    operation_summary="Fetch and assign a laborantin to a specific Bilan Biologique record.",
    responses={
        200: openapi.Response(
            description="Successfully fetched and assigned Bilan Biologique.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="A success message indicating the operation was successful.",
                        example="Laborantin successfully assigned to Bilan Biologique."
                    ),
                    'bilan': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        description="Details of the assigned Bilan Biologique.",
                        properties={
                            'bilan_id': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="Unique ID of the Bilan Biologique.",
                                example=321
                            ),
                            'laborantin_id': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="ID of the assigned laborantin.",
                                example=45
                            ),
                            'consultation_id': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="ID of the associated consultation.",
                                example=567
                            ),
                            'param_valeur': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                description="List of associated ParamValeur data for the Bilan.",
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'param_name': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Name of the parameter.",
                                            example="Glucose Level"
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
                                            description="Reference range for the parameter value.",
                                            example="3.5-6.0"
                                        )
                                    }
                                )
                            )
                        }
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Error occurred while fetching or assigning the Bilan Biologique.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error message explaining why the request failed.",
                        example="Invalid Bilan ID or laborantin ID."
                    )
                }
            )
        ),
        404: openapi.Response(
            description="Bilan Biologique not found.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error message indicating the Bilan was not found.",
                        example="No Bilan Biologique found with the provided ID."
                    )
                }
            )
        )
    }
)