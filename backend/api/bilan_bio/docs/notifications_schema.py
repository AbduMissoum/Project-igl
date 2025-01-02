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
                        type=openapi.TYPE_ARRAY,
                        description="List of serialized Bilan Biologique records.",
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description="Unique ID of the Bilan Biologique record.",
                                    example=1
                                ),
                                'consultation': openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    description="Details of the associated consultation.",
                                    properties={
                                        'patient': openapi.Schema(
                                            type=openapi.TYPE_OBJECT,
                                            description="Details of the patient.",
                                            properties={
                                                'id': openapi.Schema(
                                                    type=openapi.TYPE_INTEGER,
                                                    description="Patient's unique ID.",
                                                    example=101
                                                ),
                                                'nss': openapi.Schema(
                                                    type=openapi.TYPE_STRING,
                                                    description="Patient's NSS (National Social Security).",
                                                    example="123456789"
                                                )
                                            }
                                        ),
                                        'medcin': openapi.Schema(
                                            type=openapi.TYPE_OBJECT,
                                            description="Details of the associated medcin.",
                                            properties={
                                                'id': openapi.Schema(
                                                    type=openapi.TYPE_INTEGER,
                                                    description="Medcin's unique ID.",
                                                    example=201
                                                ),
                                                'name': openapi.Schema(
                                                    type=openapi.TYPE_STRING,
                                                    description="Name of the medcin.",
                                                    example="Dr. Jane Smith"
                                                )
                                            }
                                        )
                                    }
                                ),
                                'date': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    format=openapi.FORMAT_DATE,
                                    description="Date of the Bilan Biologique record.",
                                    example="2024-12-30"
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
                        example="Laborantin not found or another issue occurred."
                    )
                }
            )
        )
    }
)