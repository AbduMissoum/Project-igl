from django.urls import path
from . import views

urlpatterns = [
    path('consultations/', views.consultation_list, name='consultation-list'),
    path('consultations/<int:pk>/', views.consultation_detail, name='consultation-detail'),
    path('consultations/by-dpi/<int:pk>/', views.consultation_by_dpi, name='consultation_by_dpi'),
    path('consultations/<int:pk>/resume/', views.consultation_resume, name='consultation_resume'),
]
"""{
    "etablisement": "esi",
    "dpi": 3,
    "la_date": "2024-06-01"
   }
    {
    "id": 8,
    "medecin": {
        "id": 13,
        "username": "username",
        "email": "imad@esi.dz"
    },
    "dpi": {
        "id": 3,
        "qr_code": null
    },
    "etablisement": "esi",
    "resume": null,
    "la_date": "2024-06-25"
}
}"""
