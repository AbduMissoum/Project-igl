from django.urls import path
from .views import PatientList,PatientDetail,MedcinList,creer_role

urlpatterns=[
    path('',PatientList),
    path('<int:id>',PatientDetail),
    path('medecin/',MedcinList),
    path('creer',creer_role)
   
    
]
