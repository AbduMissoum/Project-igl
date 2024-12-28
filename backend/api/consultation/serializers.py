from rest_framework import serializers
from .models import Consultation
from dpi.models import Dpi
from authentication.models import CustomUser,Etablisement 


class ConsultationSerializer(serializers.ModelSerializer):
    dpi = serializers.PrimaryKeyRelatedField(queryset=Dpi.objects.all())
    medecin = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    etablisement = serializers.PrimaryKeyRelatedField(queryset=Etablisement.objects.all())

    class Meta:
        model = Consultation

        fields = ['id','dpi','medecin','etablisement','la_date','resume']

