from rest_framework.exceptions import NotFound
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.exceptions import ValidationError


def delete_soin_schema():
    """
    Returns the OpenAPI schema for deleting a soin.
    """
    return swagger_auto_schema(
        method='DELETE',
        operation_description="Delete a soin",
        responses={
            200: openapi.Response(
                description="Soin deleted successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, example='Soins deleted successfully'),
                    }
                ),
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred. Please try again later.'),
                    }
                ),
            ),
        }
    )

def patch_soin_schema():
    """
    Returns the OpenAPI schema for partially updating a soin.
    """
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'la_date': openapi.Schema(type=openapi.TYPE_STRING, format='date', example='2024-12-26'),
            'description': openapi.Schema(type=openapi.TYPE_STRING, example='Updated description'),
        },
    )

    response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'soin': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=2),
                    'description': openapi.Schema(type=openapi.TYPE_STRING, example='il doit avoir bouceau de medicament'),
                    'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='1990-01-02'),
                    'patient': openapi.Schema(type=openapi.TYPE_INTEGER, example=2),
                    'infirmier': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                }
            ),
            'message': openapi.Schema(type=openapi.TYPE_STRING, example='Soins updated successfully'),
        }
    )

    return swagger_auto_schema(
        method='PATCH',
        operation_description="Partially update a soin",
        request_body=request_body,
        responses={
            200: openapi.Response(
                description="Soin updated successfully",
                schema=response_schema,
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred. Please try again later.'),
                    }
                ),
            ),
        }
    )
def get_soin_detail_schema():
  """
  Returns the OpenAPI schema for retrieving a soin detail.

  Raises:
      NotFound: If a soin with the provided ID is not found.
  """
  schema = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=2),
          'patient': openapi.Schema(
              type=openapi.TYPE_OBJECT,
              properties={
                  'NSS': openapi.Schema(type=openapi.TYPE_STRING, example='1234567890'),
                  'nom': openapi.Schema(type=openapi.TYPE_STRING, example='NIDAl'),
                  'prenom': openapi.Schema(type=openapi.TYPE_STRING, example='Johnn'),
              }
          ),
          'infirmier': openapi.Schema(
              type=openapi.TYPE_OBJECT,
              properties={
                  'username': openapi.Schema(type=openapi.TYPE_STRING, example='NIDAl1234567890'),
                  'email': openapi.Schema(type=openapi.TYPE_STRING, example='nlmll@esi.dz'),
              }
          ),
          'description': openapi.Schema(type=openapi.TYPE_STRING, example='il doit avoir bouceau de medicament  '),
          'la_date': openapi.Schema(type=openapi.TYPE_STRING, example='1990-01-02'),
      }
  )
  return swagger_auto_schema(
      method='GET',
      operation_description="Retrieve a soin detail by its ID",
      responses={
          200: openapi.Response(
              description="Successfully retrieved soin detail",
              schema=schema,
          ),
          400: openapi.Response(
              description="Soin not found",
              schema=openapi.Schema(
                  type=openapi.TYPE_OBJECT,
                  properties={
                      'error': openapi.Schema(type=openapi.TYPE_STRING, example=f"No soins with this id {{pk}}"),
                  }
              ),
          ),
      }
  )