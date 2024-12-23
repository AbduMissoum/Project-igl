from django.db import transaction
from consultation.models import Consultation
from bilan_bio.models import BilanBiologique,ParamValeur
from authentication.models import CustomUser
from bilan_bio.serializers import ParamValeurSerializer
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
                )
                for test_name in test_names:
                    ParamValeur.objects.create(
                        parametre=test_name,
                        valeur=0.0,  # Default value
                        unite="",  # Default unit
                        bilan=bilan,
                    )
                # laboratory_users = CustomUser.objects.filter(
                #     etablisement=etablisement,
                #     role='laboratory'
                # )
                # for user in laboratory_users:
                #     Notification.objects.create(
                #         type="",
                #         descirption="",
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
            param_id = param_data.get('id')
            try:
                # Find the corresponding ParamValeur instance
                param = param_valeurs.get(id=param_id)
                # Serialize and update the ParamValeur instance
                serializer = ParamValeurSerializer(param, data=param_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return {"status": "error", "message": f"Invalid data for ParamValeur {param_id}"}
            except ParamValeur.DoesNotExist:
                return {"status": "error", "message": f"ParamValeur with id {param_id} not found"}

        # Update the laborantient and satisfait fields
        laborantient_id = data.get('laborantient')
        if laborantient_id:
            try:
                laborantient = CustomUser.objects.get(id=laborantient_id, role='laboratory')
                bilan_biologique.laborantient = laborantient
                bilan_biologique.satisfait = True
                bilan_biologique.save()
            except CustomUser.DoesNotExist:
                return {"status": "error", "message": "Laborantient user not found or invalid role"}

        # Return success if all operations complete without errors
        return {"status": "success"}

    except BilanBiologique.DoesNotExist:
        return {"status": "error", "message": "Bilan not found"}
    except Exception as e:
        # Catch unexpected errors and return a detailed message
        return {"status": "error", "message": str(e)}



