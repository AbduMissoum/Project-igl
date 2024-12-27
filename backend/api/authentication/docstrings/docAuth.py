from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def logout_schema():
  """
  Returns the OpenAPI schema for user logout.
  """
  return swagger_auto_schema(
      method='POST',
      operation_description="User logout",
      responses={
          200: openapi.Response(
              description="User logged out successfully",
              schema=openapi.Schema(
                  type=openapi.TYPE_OBJECT,
                  properties={
                      'message': openapi.Schema(type=openapi.TYPE_STRING, example='User logged out successfully'),
                  }
              ),
          ),
          400: openapi.Response(
              description="Bad Request",
              schema=openapi.Schema(
                  type=openapi.TYPE_OBJECT,
                  properties={
                      'error': openapi.Schema(type=openapi.TYPE_STRING, example='An unexpected error occurred.'),
                  }
              ),
          ),
      }
  )
def login_schema():
  """
  Returns the OpenAPI schema for user login.
  """
  request_body = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      required=['username', 'password'],
      properties={
          'username': openapi.Schema(type=openapi.TYPE_STRING, example='username'),
          'password': openapi.Schema(type=openapi.TYPE_STRING, example='password'),
      }
  )

  response_schema_200 = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'message': openapi.Schema(type=openapi.TYPE_STRING, example='User authenticated'),
          'role': openapi.Schema(type=openapi.TYPE_STRING, example='patient'),
          'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
      }
  )

  response_schema_400 = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'message': openapi.Schema(type=openapi.TYPE_STRING, example='key is missing username'),
      }
  )

  response_schema_404 = openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
          'message': openapi.Schema(type=openapi.TYPE_STRING, example='invalid credentials'),
      }
  )

  return swagger_auto_schema(
      method='POST',
      operation_description="User login",
      request_body=request_body,
      responses={
          200: openapi.Response(
              description="Login successful",
              schema=response_schema_200,
          ),
          400: openapi.Response(
              description="Bad Request",
              schema=response_schema_400,
          ),
          404: openapi.Response(
              description="Not Found",
              schema=response_schema_404,
          ),
      }
  )