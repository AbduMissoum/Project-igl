from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def ordonnance_list_schema():
    """
    Returns the OpenAPI schema for retrieving a list of ordonnances.
    """
    ordonnance_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'valide': openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of ordonnances",
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of ordonnances",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=ordonnance_schema,
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

def create_ordonnance_schema():
    """
    Returns the OpenAPI schema for creating a new ordonnance, including consultation and traitements.
    """
    # Schéma de la requête pour créer une ordonnance
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'consultation': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),  # ID de la consultation
            'traitements': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example="500mg"),  # Dose du médicament
                        'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example="7 jours"),  # Durée du traitement
                        'medicament': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'nom': openapi.Schema(type=openapi.TYPE_STRING, example="Ibuprofène")  # Nom du médicament
                            }
                        ),
                    }
                )
            ),
        }
    )

    # Schéma de la réponse après la création de l'ordonnance
    response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),  # ID de l'ordonnance
            'valide': openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),  # Validité de l'ordonnance
            'consultation': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),  # Consultation associée
            'traitements': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example="500mg"),  # Dose du médicament
                        'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example="7 jours"),  # Durée du traitement
                        'medicament': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'nom': openapi.Schema(type=openapi.TYPE_STRING, example="Ibuprofène")  # Nom du médicament
                            }
                        ),
                    }
                )
            ),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create a new ordonnance, including consultation and treatments.",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created ordonnance",
                schema=response_schema,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data.'),
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

def ordonnance_detail_schema():
    """
    Schéma OpenAPI pour la méthode GET qui récupère les détails de l'ordonnance.
    """
    response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'valide': openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
            'consultation': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'traitements': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example="500mg"),
                        'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example="7 jours"),
                        'medicament': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={'nom': openapi.Schema(type=openapi.TYPE_STRING, example="Ibuprofène")}
                        ),
                    }
                )
            ),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve the details of an ordonnance.",
        responses={200: openapi.Response(description="Successfully retrieved ordonnance", schema=response_schema)},
    )

def valider_ordonnance_schema():
    """
    Schéma OpenAPI pour la méthode POST qui valide une ordonnance.
    """
    response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'valide': openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
            'consultation': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'traitements': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example="500mg"),
                        'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example="7 jours"),
                        'medicament': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={'nom': openapi.Schema(type=openapi.TYPE_STRING, example="Ibuprofène")}
                        ),
                    }
                )
            ),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Validate an ordonnance by setting its 'valide' status to True.",
        responses={200: openapi.Response(description="Successfully validated ordonnance", schema=response_schema)},
    )

def update_ordonnance_schema():
    """
    Schéma OpenAPI pour la méthode PUT qui met à jour une ordonnance existante.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'consultation': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'traitements': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example="500mg"),
                        'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example="7 jours"),
                        'medicament': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={'nom': openapi.Schema(type=openapi.TYPE_STRING, example="Ibuprofène")}
                        ),
                    }
                )
            ),
        }
    )

    response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'valide': openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
            'consultation': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'traitements': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example="500mg"),
                        'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example="7 jours"),
                        'medicament': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={'nom': openapi.Schema(type=openapi.TYPE_STRING, example="Ibuprofène")}
                        ),
                    }
                )
            ),
        }
    )

    # Gestion des erreurs de validation du serializer
    error_response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data provided'),
            'details': openapi.Schema(type=openapi.TYPE_OBJECT, example={'field_name': 'error_message'})
        }
    )

    return swagger_auto_schema(
        method='PUT',
        operation_description="Update an existing ordonnance.",
        request_body=request_body,
        responses={
            200: openapi.Response(description="Successfully updated ordonnance", schema=response_schema),
            400: openapi.Response(description="Bad Request - Invalid data provided", schema=error_response_schema),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred')}
                ),
            ),
        },
    )
def sup_ordonnance_schema():
    """
    Schéma OpenAPI pour la méthode DELETE qui supprime une ordonnance.
    """
    response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, example="Consultation deleted successfully"),
        }
    )

    return swagger_auto_schema(
        method='DELETE',
        operation_description="Delete an ordonnance.",
        responses={200: openapi.Response(description="Successfully deleted ordonnance", schema=response_schema)},
    )

def traitement_list_schema():
    """
    Returns the OpenAPI schema for retrieving the list of treatments and creating a new treatment.
    """
    traitement_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of treatments",
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of treatments",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=traitement_schema,
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

def post_traitement_schema():
    """
    Returns the OpenAPI schema for creating a new treatment.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create a new treatment",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created treatment",
                schema=request_body,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data.'),
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

def traitement_list_schema():
    """
    Returns the OpenAPI schema for retrieving the list of treatments and creating a new treatment.
    """
    traitement_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of treatments",
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of treatments",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=traitement_schema,
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

def post_traitement_schema():
    """
    Returns the OpenAPI schema for creating a new treatment.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create a new treatment",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created treatment",
                schema=response_body,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data.'),
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

def traitement_detail_schema():
    """
    Returns the OpenAPI schema for retrieving, updating, and deleting a treatment by ID.
    """
    traitement_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a treatment by ID",
        responses={
            200: openapi.Response(
                description="Successfully retrieved treatment details",
                schema=traitement_schema,
            ),
            404: openapi.Response(
                description="Treatment not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Treatment not found.'),
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

def put_traitement_schema():
    """
    Returns the OpenAPI schema for updating a treatment.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='100mg'),
            'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='2024-10-10'),
            'medicament': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'ordonnance': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    return swagger_auto_schema(
        method='PUT',
        operation_description="Update a treatment by ID",
        request_body=request_body,
        responses={
            200: openapi.Response(
                description="Successfully updated treatment",
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
                description="Treatment not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Treatment not found.'),
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

def delete_traitement_schema():
    """
    Returns the OpenAPI schema for deleting a treatment by ID.
    """
    return swagger_auto_schema(
        method='DELETE',
        operation_description="Delete a treatment by ID",
        responses={
            204: openapi.Response(description="Successfully deleted treatment"),
            404: openapi.Response(
                description="Treatment not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Treatment not found.'),
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

def medicament_list_schema():
    """
    Returns the OpenAPI schema for retrieving the list of medications and creating a new medication.
    """
    medicament_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'nom': openapi.Schema(type=openapi.TYPE_STRING, example='Paracétamol'),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of medications",
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of medications",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=medicament_schema,
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
def post_medicament_schema():
    """
    Returns the OpenAPI schema for creating a new medication.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'nom': openapi.Schema(type=openapi.TYPE_STRING, example='Paracétamol'),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'nom': openapi.Schema(type=openapi.TYPE_STRING, example='Paracétamol'),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="Create a new medication",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Successfully created medication",
                schema=response_body,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid data.'),
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
def put_medicament_schema():
    """
    Returns the OpenAPI schema for updating a medication.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'nom': openapi.Schema(type=openapi.TYPE_STRING, example='Paracétamol 500mg'),
        }
    )
    response_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=42),  # Inclure l'ID dans la réponse
            'nom': openapi.Schema(type=openapi.TYPE_STRING, example='Paracétamol'),
        }
    )

    return swagger_auto_schema(
        method='PUT',
        operation_description="Update a medication by ID",
        request_body=request_body,
        responses={
            200: openapi.Response(
                description="Successfully updated medication",
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
                description="Medicament not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Medicament not found.'),
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
def delete_medicament_schema():
    """
    Returns the OpenAPI schema for deleting a medication by ID.
    """
    return swagger_auto_schema(
        method='DELETE',
        operation_description="Delete a medication by ID",
        responses={
            204: openapi.Response(description="Successfully deleted medication"),
            404: openapi.Response(
                description="Medicament not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Medicament not found.'),
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
def medicament_detail_schema():
    """
    Returns the OpenAPI schema for retrieving, updating, and deleting a medication by ID.
    """
    medicament_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'nom': openapi.Schema(type=openapi.TYPE_STRING, example='Paracétamol'),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a medication by ID",
        responses={
            200: openapi.Response(
                description="Successfully retrieved medication details",
                schema=medicament_schema,
            ),
            404: openapi.Response(
                description="Medicament not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Medicament not found.'),
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
def ordonnances_by_consultation_schema():
    """
    Returns the OpenAPI schema for retrieving a list of ordonnances for a specific consultation.
    """
    ordonnance_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
            'valide': openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
            'consultation': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            'traitements': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'la_dose': openapi.Schema(type=openapi.TYPE_STRING, example='500mg'),
                        'la_durre': openapi.Schema(type=openapi.TYPE_STRING, example='7 jours'),
                        'medicament': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=3),
                                'nom': openapi.Schema(type=openapi.TYPE_STRING, example='Doliprane')
                            }
                        ),
                    }
                )
            ),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve all ordonnances for a specific consultation",
        responses={ 
            200: openapi.Response(
                description="Successfully retrieved ordonnances for the consultation",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=ordonnance_schema
                ),
            ),
            404: openapi.Response(
                description="Consultation not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, example="Consultation not found")
                    }
                ),
            ),
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example="An unexpected error occurred.")
                    }
                ),
            ),
        }
    )
