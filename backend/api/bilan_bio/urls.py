from django.urls import path
from .views import demander_bilan,remplir_bilan,get_bilan,get_demandes,get_bilan_by_consultation_id

urlpatterns = [
    path('demande',demander_bilan),
    path('remplir/<int:bilan_id>/',remplir_bilan),
    path('voir-bilan/<int:bilan_id>/',get_bilan),
    path('notifications',get_demandes),
    path('details-bilan/<int:consultation_id>/',get_bilan_by_consultation_id),
]
