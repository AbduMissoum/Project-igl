from django.db import transaction
from consultation.models import Consultation
from bilan_bio.models import BilanBiologique,ParamValeur
from authentication.models import CustomUser
from bilan_bio.serializers import ParamValeurSerializer,BilanBiologiqueSerializer
from datetime import datetime
def faire_demande(test_names:list,id:int):
    try:
        with transaction.atomic():
                # Get the consultation
                consultation = Consultation.objects.get(id=id)
                medecin = consultation.medecin
                etablisement = consultation.etablisement

                # Create the BilanBiologique instance
                bilan = BilanBiologique.objects.create(
                    description=None,
                    consultation=consultation,
                    laborantient=None,  
                    satisfait=False,
                    date = datetime.now()
                )
                for test_name in test_names:
                    ParamValeur.objects.create(
                        parametre=test_name,
                        valeur=0.0,  # Default value
                        unite="",  # Default unit
                        bilan=bilan,
                    )
                # laboratory_users = CustomUser.objects.filter(
                # etablisement=etablisement,
                # role='laboratory'
                # )
                # for user in laboratory_users:
                #     Notification.objects.create(
                #         type="Bilan Created",
                #         descirption=f"A new bilan has been created for consultation {consultation.id}",
                #         read=False,
                #     )
               
        return {"status": "success", "bilan_id": bilan.id}

    except Consultation.DoesNotExist:
        return {"status": "error", "message": "Consultation not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def remplissement_bilan(id: int, data):
    try:
        bilan_biologique = BilanBiologique.objects.get(id=id)
        param_valeurs = ParamValeur.objects.filter(bilan=bilan_biologique)
        param_valeurs_data = data.get('param_valeurs', [])

        # Update each ParamValeur instance
        for param_data in param_valeurs_data:
            param_name = param_data.get('parametre')
            try:
                # Find the corresponding ParamValeur instance
                param = param_valeurs.get(parametre=param_name)
                # Serialize and update the ParamValeur instance
                serializer = ParamValeurSerializer(param, data=param_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return {"status": "error", "message": f"Invalid data for ParamValeur {param_name}"}
            except ParamValeur.DoesNotExist:
                return {"status": "error", "message": f"ParamValeur with id {param_name} not found"}

        # Update the satisfait fields  
            # bilan_biologique.laborantient = laborantient
        bilan_biologique.satisfait = True
        bilan_biologique.save()
            

        # Return success if all operations complete without errors
        return {"status": "success"}

    except BilanBiologique.DoesNotExist:
        return {"status": "error", "message": "Bilan not found"}
    except Exception as e:
        # Catch unexpected errors and return a detailed message
        return {"status": "error", "message": str(e)}
def fetch_bilan(id:int,lab_id:int):
    try:
        bilan = BilanBiologique.objects.get(id=id)
        user = CustomUser.objects.get(id=lab_id)
        consultation = bilan.consultation
        if user.role == 'laborantin':
            if bilan.laborantient == None or bilan.laborantient == user:
                bilan.laborantient=user
                bilan.save()
            else:
                raise PermissionError("You do not have permission to see this bilan")
        params = ParamValeur.objects.filter(bilan=bilan)
        serializer = ParamValeurSerializer(params, many=True)
        return {"status": "success", "message": serializer.data}
    except BilanBiologique.DoesNotExist:
        return {"status": "error", "message": f"BilanBiologique with ID {id} not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
def fetch_non_assigned(id:int):
    try:
        laborantin = CustomUser.objects.get(id=id)  
        bilans = BilanBiologique.objects.filter(satisfait=False,laborantient=None,consultation__etablisement=laborantin.etablisement)
        print(bilans)
        serializer = BilanBiologiqueSerializer(bilans,many=True)
        return {"status":"success","message":serializer.data}
    except Exception as e:
        return {"status":"error","message":str(e)}
def check_bilan(consultation_id:int,user_id:int,user):
    try:

        print(consultation_id)
        print(user_id)
        consultation = Consultation.objects.get(id=int(consultation_id))
        print(consultation)
        bilan = BilanBiologique.object.get(consultation=consultation)
        print(bilan)
        user = CustomUser.objects.get(id=user_id)

        if user.role == 'medecin' and user!=consultation.medecin:
            raise PermissionError("You do not have permission to see this bilan")
        elif user.role == 'patient' and consultation.dpi.id.id !=user:
            raise PermissionError("You do not have permission to see this bilan")
        params = ParamValeur.objects.filter(bilan=bilan)
        serializer = ParamValeurSerializer(params, many=True)
        return {"status": "success", "message": serializer.data}
    except Consultation.DoesNotExist:
        return {"status": "error", "message": f"Consultation with ID {consultation_id} not found"}
    except BilanBiologique.DoesNotExist:
        return {"status":"error","message":"Bilan for this consultation doesn't exist"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
