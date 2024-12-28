from django.urls import path
from .views import PatientList,PatientDetail,MedcinList

urlpatterns=[
    path('',PatientList),
    path('<int:id>',PatientDetail),
    path('medecin/',MedcinList)
   
    
]
