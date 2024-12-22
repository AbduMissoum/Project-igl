from rest_framework import serializers
from .models import Patient,Dpi
from authentication.models import CustomUser
from authentication.serializers import UserSerializer

class PatientCreateSerializer(serializers.ModelSerializer):
   
    class Meta:
       model= Patient
       exclude  = ('id',)
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
       model= Patient
       fields = '__all__'
class UserListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "username": value.username,
            "email": value.email,
        }
    class Meta:
        model = CustomUser
        fields = ['username']
    
class PatientSerializerWithId(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'
    medecin_traitant = UserListingField(many=True, read_only=True)

   
   
    
       
    