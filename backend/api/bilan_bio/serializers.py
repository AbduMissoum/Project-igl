from rest_framework import serializers
from .models import ParamValeur
from rest_framework import serializers
from .models import ParamValeur

class ParamValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamValeur
        fields = ['id', 'parametre', 'valeur', 'unite']

    def update(self, instance, validated_data):
        # Update the instance with new values from validated_data
        instance.valeur = validated_data.get('valeur', instance.valeur)
        instance.unite = validated_data.get('unite', instance.unite)
        instance.save()
        return instance

