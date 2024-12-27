from django.urls import path
from . import views

urlpatterns = [
    path('', views.soins_list, name='soins-list'),
    path('<int:pk>/', views.soins_detail, name='soins-detail'),
    path('patient/<int:patient_id>/', views.soins_list_by_patient_id, name='soins-list-by-patient-id'),
    path('infirmier/', views.soins_with_infirmier, name='soins-with-infirmier'),
]
