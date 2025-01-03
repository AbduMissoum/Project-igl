from django.urls import path
from . import views

urlpatterns = [
    path('medicaments/', views.medicament_list, name='medicament_list'),
    path('medicaments/<int:pk>/', views.medicament_detail, name='medicament_detail'),
    path('ordonnances/', views.ordonnance_create, name='ordonnance_create'),
    path('ordonnances/<int:pk>/', views.ordonnance_detail, name='ordonnance_detail'),
    path('ordonnances/consultation/<int:consultation_id>/', views.ordonnances_by_consultation, name='ordonnances_by_consultation'),
    path('traitements/', views.traitement_list, name='traitement_list'),
    path('traitements/<int:pk>/', views.traitement_detail, name='traitement_detail'),
    path('ordonnances/<int:pk>/valider/', views.valider_ordonnance, name='valider_ordonnance'),
]
"""{
    "consultation": 1,
    "traitements": [
        {
            "la_dose": "500mg",
            "la_durre": "7 jours",
            "medicament": {"nom": "Ibuprofène"}
        },
        {
            "la_dose": "250mg",
            "la_durre": "3 jours",
            "medicament": {"nom": "Paracétamol"}
        }
    ]
}

[
    {
        "id": 1,
        "valide": false,
        "consultation": 1,
        "traitements": []
    },
    {
        "id": 5,
        "valide": false,
        "consultation": 1,
        "traitements": [
            {
                "la_dose": "500mg",
                "la_durre": "7 jours",
                "medicament": {
                    "id": 3,
                    "nom": "doliprane"
                }
            },
            {
                "la_dose": "250mg",
                "la_durre": "3 jours",
                "medicament": {
                    "id": 1,
                    "nom": "Paracétamol"
                }
            }
        ]
    },
    {
        "id": 6,
        "valide": true,
        "consultation": 1,
        "traitements": [
            {
                "la_dose": "500mg",
                "la_durre": "7 jours",
                "medicament": {
                    "id": 3,
                    "nom": "doliprane"
                }
            },
            {
                "la_dose": "250mg",
                "la_durre": "3 jours",
                "medicament": {
                    "id": 1,
                    "nom": "Paracétamol"
                }
            }
        ]
    }
]

"""
