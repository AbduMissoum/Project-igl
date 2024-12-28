from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from bilan_bio.serializers import RemplirBilanRequestSerializer
def remplir_schema():
    return swagger_auto_schema(
    method='put',
    operation_description="Fill in a Bilan Biologique with the provided parameters. Requires permission to modify the Bilan.",
    operation_summary="Fill in a Bilan Biologique",
    request_body=RemplirBilanRequestSerializer,
    responses={
        201: openapi.Response("Bilan Satisfied"),
        403: openapi.Response("Permission Denied"),
        400: openapi.Response("Bad Request"),
    },
)