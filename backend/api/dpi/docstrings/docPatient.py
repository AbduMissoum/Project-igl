from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def medecin_list_schema():
  """
  Returns the OpenAPI schema for retrieving a list of medecin objects.
  """
  medecin_schema = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=7),
          'username': openapi.Schema(type=openapi.TYPE_STRING, example='medein'),
          'email': openapi.Schema(type=openapi.TYPE_STRING, example='medecin@gmail.com'),
      }
  )

  return swagger_auto_schema(
      method='GET',
      operation_description="Retrieve a list of medecin",
      responses={
          200: openapi.Response(
              description="Successfully retrieved list of medecin",
              schema=openapi.Schema(
                  type=openapi.TYPE_ARRAY,
                  items=medecin_schema,
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
def create_patient_schema():
  """
  Returns the OpenAPI schema for creating a new patient.
  """
  request_body = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'NSS': openapi.Schema(type=openapi.TYPE_STRING, example='1234567k8904'),
          'nom': openapi.Schema(type=openapi.TYPE_STRING, example='NIDAl'),
          'prenom': openapi.Schema(type=openapi.TYPE_STRING, example='Johnn'),
          'date_naissance': openapi.Schema(type=openapi.TYPE_STRING, format='date', example='1990-01-02'),
          'adress': openapi.Schema(type=openapi.TYPE_STRING, example='123 Main Street, City, Country'),
          'tel': openapi.Schema(type=openapi.TYPE_STRING, example='1234l567890'),
          'mutuelle': openapi.Schema(type=openapi.TYPE_STRING, example='Some Insurance'),
          'medecin_traitant': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_INTEGER)), 
      }
  )

  response_schema_201 = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'message': openapi.Schema(type=openapi.TYPE_STRING, example='Patient created successfully'),
          'patient': openapi.Schema(
              type=openapi.TYPE_OBJECT,
              properties={
                  'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=9),
                  'NSS': openapi.Schema(type=openapi.TYPE_STRING, example='1234567k8904'),
                  'nom': openapi.Schema(type=openapi.TYPE_STRING, example='NIDAl'),
                  'prenom': openapi.Schema(type=openapi.TYPE_STRING, example='Johnn'),
                  'date_naissance': openapi.Schema(type=openapi.TYPE_STRING, example='1990-01-02'),
                  'adress': openapi.Schema(type=openapi.TYPE_STRING, example='123 Main Street, City, Country'),
                  'tel': openapi.Schema(type=openapi.TYPE_STRING, example='1234l567890'),
                  'mutuelle': openapi.Schema(type=openapi.TYPE_STRING, example='Some Insurance'),
                  'medecin_traitant': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_INTEGER)), 
              }
          ),
      }
  )

  response_schema_400 = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'errors': openapi.Schema(
              type=openapi.TYPE_OBJECT,
              properties={
                  'NSS': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)), 
              }
          ),
      }
  )

  return swagger_auto_schema(
      method='POST',
      operation_description="Create a new patient",
      request_body=request_body,
      responses={
          201: openapi.Response(
              description="Patient created successfully",
              schema=response_schema_201,
          ),
          400: openapi.Response(
              description="Bad Request",
              schema=response_schema_400,
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
def patient_list_by_nss_schema():
    """
    Returns the OpenAPI schema for retrieving a list of patients by NSS.
    NSS must be provided in the query parameters, e.g., patient?NSS=1234567k8904
    """
    patient_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
            'nom': openapi.Schema(type=openapi.TYPE_STRING, example='NIDAl'),
            'prenom': openapi.Schema(type=openapi.TYPE_STRING, example='Johnn'),
            'tel': openapi.Schema(type=openapi.TYPE_STRING, example='1234l567890'),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of patients by NSS. NSS must be in query parameters, e.g., patient?NSS=1234567k8904",
        query_parameters=[
            openapi.Parameter(
                'NSS',
                openapi.IN_QUERY,
                description='Patient NSS',
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                description="Successfully retrieved list of patients",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=patient_schema,
                ),
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='NSS missing'),
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

def patient_detail_schema():
  """
  Returns the OpenAPI schema for retrieving a patient by ID.
  """
  medecin_schema = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'username': openapi.Schema(type=openapi.TYPE_STRING, example='abdallah'),
          'email': openapi.Schema(type=openapi.TYPE_STRING, example='ma_missoum@esi.dz'),
      }
  )

  patient_schema = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
          'medecin_traitant': openapi.Schema(type=openapi.TYPE_ARRAY, items=medecin_schema),
          'NSS': openapi.Schema(type=openapi.TYPE_STRING, example='1234567890'),
          'nom': openapi.Schema(type=openapi.TYPE_STRING, example='NIDAl'),
          'prenom': openapi.Schema(type=openapi.TYPE_STRING, example='Johnn'),
          'date_naissance': openapi.Schema(type=openapi.TYPE_STRING, example='1990-01-02'),
          'adress': openapi.Schema(type=openapi.TYPE_STRING, example='123 Main Street, City, Country'),
          'tel': openapi.Schema(type=openapi.TYPE_STRING, example='1234l567890'),
          'mutuelle': openapi.Schema(type=openapi.TYPE_STRING, example='Some Insurance'),
      }
  )

  return swagger_auto_schema(
      method='GET',
      operation_description="Retrieve a patient by ID",
      responses={
          200: openapi.Response(
              description="Successfully retrieved patient details",
              schema=patient_schema,
          ),
          404: openapi.Response(
              description="Patient not found",
              schema=openapi.Schema(
                  type=openapi.TYPE_OBJECT,
                  properties={
                      'error': openapi.Schema(type=openapi.TYPE_STRING, example='Patient not found'),
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