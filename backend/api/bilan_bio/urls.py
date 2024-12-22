from django.urls import path
from .views import demander_bilan,remplir_bilan

urlpatterns = [
    path('demande',demander_bilan),
    path('remplir/<int:bilan_id>/',remplir_bilan)
]
