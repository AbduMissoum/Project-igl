from bilan_radio.models import BilanRadiologique,ExamenImagerieMedicale
from consultation.models import Consultation
from django.db import transaction
from authentication.models import CustomUser
from bilan_radio.Serializers import BilanRadiologiqueSerializer,ExamenImagerieMedicaleSerializer
def faire_demande(id:int,type:str):
    try:
        with transaction.atomic():
                # Get the consultation
                consultation = Consultation.objects.get(id=id)
                medecin = consultation.medecin
                etablisement = consultation.etablisement

                # Create the BilanRadiologique instance
                bilan = BilanRadiologique.objects.create(
                    type=type,
                    compte_rendu = None,
                    consultation=consultation, 
                    radiologe = None,
                )
                examen = ExamenImagerieMedicale.objects.create(
                    examen_image = None,
                    bilan = bilan,
                )
        return {"status": "success", "bilan_id": [bilan.id,examen.id]}
    except Consultation.DoesNotExist:
        return {"status": "error", "message": "Consultation not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
def fetch_bilan(id:int,rad_id:int):
    try:
        bilan = BilanRadiologique.objects.get(id=id)
        radiologe = CustomUser.objects.get(id=rad_id)
        bilan.radiologe=radiologe
        bilan.save()
        return {"status": "success", "message": "Bilan radiologique fetched successfuly"}
    except BilanRadiologique.DoesNotExist:
        return {"status": "error", "message": f"BilanBiologique with ID {id} not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
def fetch_non_assigned():
    try:
        bilans = BilanRadiologique.objects.filter(satisfait=False,radiologe=None)
        serializer = BilanRadiologiqueSerializer(bilans,many=True)
        return {"status":"success","message":serializer.data}
    except Exception as e:
        return{"status":"error","message":str(e)}
def remplissement_bilan(bilan_id:int,data):
    try:
        bilan = BilanRadiologique.objects.get(id=bilan_id)
        compte_rendu = data.get('compte_rendu')
        bilan.satisfait = True
        if compte_rendu:
            bilan.compte_rendu = compte_rendu
            bilan.save()
        examen = ExamenImagerieMedicale.objects.get(bilan=bilan)
        serializer=ExamenImagerieMedicaleSerializer(examen,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return {"status":"success","message":serializer.data}
        return {"status":"error","message":serializer.errors}
    except BilanRadiologique.DoesNotExist:
        return {"status":"error","message":f"Bilan radiologique with ID {bilan_id} does not exist"}
    except ExamenImagerieMedicale.DoesNotExist:
        return{"status":"error","message":f"Examen for bilan ID {bilan_id} does not exist"}
    except Exception as e:
        return {"status":"error","message":str(e)}