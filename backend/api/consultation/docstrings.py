from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Schema for GET request
def consultation_list_schema():
    """
    Returns the OpenAPI schema for retrieving a list of consultations.
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

# Schema for POST request
def post_consultation_schema():
    """
    Returns the OpenAPI schema for creating a new consultation.
    """
    # Schema for request body (input parameters)
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'etablisement': openapi.Schema(type=openapi.TYPE_STRING, example='esi'),  # String input for etablisement name
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=3),  # Integer input for dpi
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-06-01'),  # Date string in 'YYYY-MM-DD'
        },
        required=['etablisement', 'dpi', 'la_date']  # Required fields for the request
    )

    # Schema for response body (output)
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=10),  # ID of the created consultation
            'medecin': openapi.Schema(  # Medecin (doctor) details
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=13),
                    'username': openapi.Schema(type=openapi.TYPE_STRING, example='imad14'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, example='imad@esi.dz')
                }
            ),
            'dpi': openapi.Schema(type=openapi.TYPE_INTEGER, example=3),  # Integer input for dpi
            'etablisement': openapi.Schema(type=openapi.TYPE_STRING, example='esi'),  # Etablisement name
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example=None),  # Optional resume, could be null
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-06-01'),  # Date of consultation
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create a new consultation",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created consultation",
                schema=response_body,  # Using the response schema with the ID
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data provided.')
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.')
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
            'medecin': openapi.Schema(type=openapi.TYPE_STRING, example='imad14'),  # Medecin as a username
            'dpi': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=2),
                    'NSS': openapi.Schema(type=openapi.TYPE_STRING, example='123'),
                    'nom': openapi.Schema(type=openapi.TYPE_STRING, example='patient'),
                    'prenom': openapi.Schema(type=openapi.TYPE_STRING, example='dz'),
                }
            ),
            'etablisement': openapi.Schema(type=openapi.TYPE_STRING, example='esi'),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example=''),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-29'),
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
            'medecin': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=13),  # Medecin ID for update
                    'username': openapi.Schema(type=openapi.TYPE_STRING, example='username'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, example='imad@esi.dz'),
                }
            ),
            'dpi': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=3),
                    'qr_code': openapi.Schema(type=openapi.TYPE_STRING, example=None),
                }
            ),
            'etablisement': openapi.Schema(type=openapi.TYPE_STRING, example='esi'),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Updated consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-05'),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=8),  # Consultation ID
            'medecin': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=13),
                    'username': openapi.Schema(type=openapi.TYPE_STRING, example='username'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, example='imad@esi.dz'),
                }
            ),
            'dpi': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=3),
                    'qr_code': openapi.Schema(type=openapi.TYPE_STRING, example=None),
                }
            ),
            'etablisement': openapi.Schema(type=openapi.TYPE_STRING, example='esi'),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Updated consultation summary'),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-05'),
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


def consultation_by_dpi_get_schema():
    """
    Returns the OpenAPI schema for retrieving consultations by DPI ID.
    """
    consultation_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'medecin': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=13),
                    'username': openapi.Schema(type=openapi.TYPE_STRING, example='username'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, example='imad@esi.dz'),
                }
            ),
            'etablisement': openapi.Schema(type=openapi.TYPE_STRING, example='esi'),
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example=None),
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='2024-12-01'),
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
def consultation_resume_get_schema():
    """
    Returns the OpenAPI schema for retrieving consultation resume by ID.
    """
    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve the consultation resume by ID",
        responses={
            200: openapi.Response(
                description="Successfully retrieved consultation resume",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation resume text here')
                    }
                ),
            ),
            404: openapi.Response(
                description="Consultation not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation not found.')
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.')
                    }
                ),
            ),
        }
    )

def consultation_resume_post_schema():
    """
    Returns the OpenAPI schema for updating consultation resume by ID.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Updated consultation resume text here')
        },
        required=['resume']
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Update the consultation resume by ID",
        request_body=request_body,
        responses={
            200: openapi.Response(
                description="Successfully updated consultation resume",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, example='Resume updated successfully'),
                        'resume': openapi.Schema(type=openapi.TYPE_STRING, example='Updated consultation resume text here')
                    }
                ),
            ),
            400: openapi.Response(
                description="Bad Request - missing or invalid data",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid request format or data')
                    }
                ),
            ),
            404: openapi.Response(
                description="Consultation not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Consultation not found.')
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.')
                    }
                ),
            ),
        }
    )

