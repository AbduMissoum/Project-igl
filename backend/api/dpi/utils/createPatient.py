from dpi.serializers import PatientCreateSerializer,PatientSerializer
from authentication.models import CustomUser
from dpi.models import Dpi, Patient

def createPatient(data):
    # Validate the incoming data using the serializer
    serializer = PatientCreateSerializer(data=data)
    if serializer.is_valid():
        # Extract validated data
        validated_data = serializer.validated_data

        # Create the user account
        user = CustomUser.objects.create_user(
            username=f"{validated_data['nom']}{validated_data['NSS']}",
            password=f"{validated_data['nom']}{validated_data['prenom']}",
            email=data['email'],
        )
        print("*************************************\n\n*************************")
        print(user)
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
        dpi= Dpi.objects.create(id=patient)
        #serializing 
        res = PatientSerializer(patient)
        
        print(res.data)
        return res.data                          

       
    else:
        # Return errors if validation fails
        return {"errors": serializer.errors}
