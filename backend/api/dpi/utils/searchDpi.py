from dpi.serializers import PatientCreateSerializer,PatientSerializer
from authentication.models import CustomUser
from dpi.models import Dpi, Patient

def searchDpiNSS(request):
    nss =  request.GET.get('NSS',None)
    if nss is not None : 
     patientobj = Patient.objects.filter(NSS=nss).values("id", "nom", "prenom", "tel")
     print(patientobj)
     return patientobj
    return {"error":"NSS missing"} 
        
        
    
    
    