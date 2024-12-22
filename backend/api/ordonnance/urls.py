from django.urls import path
from . import views

urlpatterns = [
    path('medicaments/', views.medicament_list, name='medicament_list'),
    path('medicaments/<int:pk>/', views.medicament_detail, name='medicament_detail'),
    path('ordonnances/', views.ordonnance_list, name='ordonnance_list'),
    path('ordonnances/<int:pk>/', views.ordonnance_detail, name='ordonnance_detail'),
    path('traitements/', views.traitement_list, name='traitement_list'),
    path('traitements/<int:pk>/', views.traitement_detail, name='traitement_detail'),
    path('ordonnances/<int:ordonnance_pk>/traitements/', views.traitements_par_ordonnance, name='traitements_par_ordonnance'),
]
