from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import demander_bilan_radiologique,get_bilan_radiologique,get_demandes,RemplirAPIView,ExamenImagerieByConsultationView
urlpatterns = [
    path('demande',demander_bilan_radiologique),
    path('voir-bilan/<int:bilan_id>/',get_bilan_radiologique),
    path('notifications',get_demandes),
    path('remplir/<int:bilan_id>/',RemplirAPIView.as_view()),
    path('bilan-details/<int:consultation_id>/',ExamenImagerieByConsultationView.as_view())
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
