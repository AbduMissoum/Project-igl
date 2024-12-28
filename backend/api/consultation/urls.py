from django.urls import path
from . import views

urlpatterns = [
    path('consultations/', views.consultation_list, name='consultation-list'),
    path('consultations/<int:pk>/', views.consultation_detail, name='consultation-detail'),
    path('consultations/by-date/<str:date>/', views.consultation_by_date, name='consultation-by-date'),
    path('consultations/by-dpi/<int:pk>/', views.consultation_by_dpi, name='consultation_by_dpi'),
    path('consultations/medecin/<int:medecin_id>/', views.consultation_by_medecin, name='consultation_by_medecin'),
]