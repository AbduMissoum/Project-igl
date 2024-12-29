from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from bilan_bio.serializers import RemplirBilanRequestSerializer
def remplir_schema():
    return swagger_auto_schema(
    method='PUT',
    operation_description=(
        "Fill in a Bilan Biologique with the provided parameters, such as test results and notes. "
        "This operation requires appropriate permissions to modify the Bilan."
    ),
    operation_summary="Fill in a Bilan Biologique.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'bilan_id': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="ID of the Bilan Biologique to be updated.",
                example=123
            ),
            'test_results': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'test_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Name of the test being updated.",
                            example="Complete Blood Count"
                        ),
                        'valeur': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Result of the test.",
                            example="10"
                        ),
                        'unite': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Unit of measurement for the result, if applicable.",
                            example="mg/dL"
                        ),
                        'valeur_reference': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Reference range for the test result.",
                            example="4.5-11.0"
                        )
                    }
                ),
                description="List of test results for the Bilan Biologique."
            ),
            'notes': openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Additional notes or observations for the Bilan.",
                example="Patient shows improvement compared to last test results."
            )
        },
        required=['bilan_id', 'test_results']
    ),
    responses={
        201: openapi.Response(
            description="Bilan updated successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Success message indicating the Bilan was updated.",
                        example="Bilan Biologique has been updated successfully."
                    ),
                    'bilan_id': openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="ID of the updated Bilan.",
                        example=123
                    )
                }
            )
        ),
        403: openapi.Response(
            description="Permission denied.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error message indicating lack of permissions.",
                        example="You do not have permission to modify this Bilan."
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Invalid request data.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error message indicating why the request failed.",
                        example="Invalid Bilan ID or missing required fields."
                    )
                }
            )
        )
    }
)