from django.urls import path
from .views import PatientList,PatientDetail

urlpatterns=[
    path('',PatientList),
    path('<int:id>',PatientDetail)
   
    
]
