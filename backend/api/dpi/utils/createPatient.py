from dpi.serializers import PatientCreateSerializer,PatientSerializer,DpiSerializer
from authentication.models import CustomUser
from dpi.models import Dpi, Patient
import random,string

def createPatient(data):
    # Validate the incoming data using the serializer
    serializer = PatientCreateSerializer(data=data)
    if serializer.is_valid():
        # Extract validated data
        validated_data = serializer.validated_data

        # Create the user account
        password = ''.join(random.choices(string.ascii_letters, k=10))

        user = CustomUser.objects.create_user(
            username=f"{validated_data['nom']}{validated_data['NSS']}",
            password=password,
            email=data['email'],
        )
      
        # Save the Patient instance
        patientwithoutId = serializer.validated_data
        patient = Patient.objects.create(
                  id=user,
                tel=patientwithoutId["tel"],
    NSS=patientwithoutId["NSS"],
    nom=patientwithoutId["nom"],
    prenom=patientwithoutId["prenom"],
    date_naissance=patientwithoutId["date_naissance"],
    adress=patientwithoutId["adress"],  # Corrected to use dictionary key access
    mutuelle=patientwithoutId.get("mutuelle"),  # Use .get() for optional fields
)
     
                                          
        patient.medecin_traitant.set(patientwithoutId["medecin_traitant"])                               
        patient.save() 
        #creating dpi
        #serializing 
        res = PatientSerializer(patient)
        dpi = DpiSerializer(data=res.data)
        if dpi.is_valid():
            dpi.save()
        else: return {"errors": dpi.errors}
        
        return { "username": user.username, 
                "password": password,
                "email":user.email,
                "patient":res.data}                          

       
    else:
        # Return errors if validation fails
        return {"errors": serializer.errors}
