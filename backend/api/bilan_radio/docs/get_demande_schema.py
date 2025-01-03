from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def get_demandes_schema():
    """
    Returns a swagger_auto_schema decorator for the get_demandes endpoint
    """
    return swagger_auto_schema(
    method='GET',
    operation_description="Fetch non-assigned Bilan Radiologique records for the authenticated radiologue user. This endpoint retrieves all Bilans that have not yet been assigned to any radiologue.",
    operation_summary="Fetch all non-assigned Bilan Radiologique records.",
    responses={
        200: openapi.Response(
            description="Successfully fetched non-assigned Bilans.",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Unique identifier of the Bilan Radiologique.",
                            example=3
                        ),
                        'consultation': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'patient': openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'NSS': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="The National Social Security number of the patient.",
                                            example="mllmLlmlk99922"
                                        ),
                                        'nom': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="The last name of the patient.",
                                            example="NIDAl"
                                        ),
                                        'prenom': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="The first name of the patient.",
                                            example="Johnn"
                                        )
                                    }
                                ),
                                'medcin': openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'username': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="The username of the medcin.",
                                            example="nidal"
                                        ),
                                        'email': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="The email address of the medcin.",
                                            example="nidhal@gmail.com"
                                        )
                                    }
                                )
                            }
                        ),
                        'date': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format="date",
                            description="The date associated with the Bilan Radiologique.",
                            example="2025-01-03"
                        )
                    }
                )
            )
        ),
        400: openapi.Response(
            description="Error occurred while fetching non-assigned Bilans.",
            schema=openapi.Schema(
                type=openapi.TYPE_STRING,
                example="CustomUser matching query does not exist."
            )
        )
    }
)