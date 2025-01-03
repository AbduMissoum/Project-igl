from rest_framework import serializers
from .models import Ordonnance, Traitement, Medicament

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = ['id', 'nom']  # Inclut uniquement les champs nécessaires

class TraitementSerializer(serializers.ModelSerializer):
    medicament = MedicamentSerializer()  # Permet de traiter les informations du médicament

    class Meta:
        model = Traitement
        fields = ['la_dose', 'la_durre', 'medicament']

class OrdonnanceSerializer(serializers.ModelSerializer):
    traitements = TraitementSerializer(many=True)  # Permet d'associer plusieurs traitements

    class Meta:
        model = Ordonnance
        fields = ['id', 'valide', 'consultation', 'traitements']
        read_only_fields = ['valide']  # Champ défini automatiquement à False

    def create(self, validated_data):
        traitements_data = validated_data.pop('traitements')  # Extraire les traitements
        ordonnance = Ordonnance.objects.create(**validated_data, valide=False)  # Toujours à False

        for traitement_data in traitements_data:
            medicament_data = traitement_data.pop('medicament')
            medicament, _ = Medicament.objects.get_or_create(**medicament_data)  # Crée ou récupère un médicament
            Traitement.objects.create(
                ordonnance=ordonnance,
                medicament=medicament,
                **traitement_data
            )

        # Rafraîchir l'objet pour inclure les relations
        ordonnance.refresh_from_db()
        return ordonnance
    def update(self, instance, validated_data):
        # Mettre à jour l'ordonnance elle-même
        instance.consultation = validated_data.get('consultation', instance.consultation)
        instance.save()

        # Mettre à jour ou créer les traitements
        traitements_data = validated_data.get('traitements', [])
        
        # Supprimer les anciens traitements s'ils ne sont pas dans la nouvelle liste
        existing_traitements = {traitement.id: traitement for traitement in instance.traitements.all()}
        for traitement_data in traitements_data:
            traitement_id = traitement_data.get('id')
            if traitement_id:
                # Mettre à jour un traitement existant
                traitement = existing_traitements.pop(traitement_id, None)
                if traitement:
                    # Mettre à jour les champs du traitement
                    traitement.la_dose = traitement_data.get('la_dose', traitement.la_dose)
                    traitement.la_durre = traitement_data.get('la_durre', traitement.la_durre)
                    traitement.save()
            else:
                # Créer un nouveau traitement
                medicament_data = traitement_data.pop('medicament')
                medicament, _ = Medicament.objects.get_or_create(**medicament_data)
                Traitement.objects.create(
                    ordonnance=instance,
                    medicament=medicament,
                    **traitement_data
                )

        # Supprimer les traitements existants qui ne sont plus dans la liste
        for traitement in existing_traitements.values():
            traitement.delete()

        return instance
  
