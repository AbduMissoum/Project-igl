from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def consultation_list_schema():
    """
    Returns the OpenAPI schema for retrieving a list of consultations and creating a new consultation.
    """
    consultation_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of consultations",
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of consultations",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=consultation_schema,
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
def post_consultation_schema():
    """
    Returns the OpenAPI schema for creating a new consultation.
    """
    # Schéma pour la requête
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation details'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        },
        required=['dpi', 'resume', 'la_date', 'medecin', 'etablisement']  # Champs obligatoires
    )

    # Schéma pour la réponse
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation details'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create a new consultation",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created consultation",
                schema=response_body,  # Utilisation du schéma avec l'ID
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data provided.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )

def consultation_detail_schema():
    """
    Returns the OpenAPI schema for retrieving, updating, and deleting a consultation by ID.
    """
    consultation_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a consultation by ID",
        responses={
            200: openapi.Response(
                description="Successfully retrieved consultation details",
                schema=consultation_schema,
            ),
            404: openapi.Response(
                description="Consultation not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation not found.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
def put_consultation_schema():
    """
    Returns the OpenAPI schema for updating a consultation by ID.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Updated consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-05'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation details'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='PUT',
        operation_description="Update a consultation by ID",
        request_body=request_body,
        responses={
            200: openapi.Response(
                description="Successfully updated consultation",
                schema=response_body,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data provided.'),
                    }
                ),
            ),
            404: openapi.Response(
                description="Consultation not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation not found.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
def delete_consultation_schema():
    """
    Returns the OpenAPI schema for deleting a consultation by ID.
    """
    return swagger_auto_schema(
        method='DELETE',
        operation_description="Delete a consultation by ID",
        responses={
            204: openapi.Response(description="Successfully deleted consultation"),
            404: openapi.Response(
                description="Consultation not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation not found.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
def consultation_by_date_get_schema():
    """
    Returns the OpenAPI schema for retrieving consultations by date and creating new consultations by date.
    """
    consultation_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve consultations by date",
        responses={
            200: openapi.Response(
                description="Successfully retrieved consultations by date",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=consultation_schema,
                ),
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid date format.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
def consultation_by_medecin_get_schema():
    """
    Returns the OpenAPI schema for retrieving consultations associated with a specific doctor (medecin).
    """
    consultation_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve consultations associated with a specific doctor (medecin)",
        responses={
            200: openapi.Response(
                description="Successfully retrieved consultations by doctor",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=consultation_schema,
                ),
            ),
            404: openapi.Response(
                description="Doctor not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Doctor not found.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
def consultation_by_medecin_post_schema():
    """
    Returns the OpenAPI schema for creating consultations associated with a specific doctor (medecin).
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation details'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation details'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create consultations associated with a specific doctor (medecin)",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created consultation",
                schema=response_body,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data provided.'),
                    }
                ),
            ),
            404: openapi.Response(
                description="Doctor not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Doctor not found.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )

def consultation_by_dpi_post_schema():
    """
    Returns the OpenAPI schema for creating consultations by DPI ID.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation details'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation details'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create consultations associated with a specific DPI.",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created consultations for DPI",
                schema=response_body,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data provided.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
def consultation_by_dpi_get_schema():
    """
    Returns the OpenAPI schema for retrieving consultations by DPI ID.
    """
    consultation_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
            'medecin': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'etablisement': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve consultations associated with a specific DPI.",
        responses={
            200: openapi.Response(
                description="Successfully retrieved consultations for DPI",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=consultation_schema,
                ),
            ),
            404: openapi.Response(
                description="DPI not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='DPI not found.'),
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                    }
                ),
            ),
        }
    )
