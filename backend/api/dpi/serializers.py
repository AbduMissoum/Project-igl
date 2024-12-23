from rest_framework import serializers
from .models import Patient,Dpi
from authentication.models import CustomUser
from authentication.serializers import UserSerializer
import qrcode
from io import BytesIO
import qrcode
from PIL import Image
from django.core.files import File
import base64

from django.utils import timezone as data
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

class PatientSerializerWithNSS(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = ['NSS','nom','prenom']
   
    
       
class DpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dpi
        fields = '__all__'
  
    def create(self, validated_data):
        # Create the model instance
        dpi_instance = Dpi.objects.create(**validated_data)
        print(dpi_instance.id.NSS)
        # Generate the QR code
        qrcode_img = qrcode.make(dpi_instance.id.NSS).convert('RGB')  # Convert to RGB mode

        # Create a blank white canvas
        canvas = Image.new('RGB', (290, 290), (255, 255, 255))

        # Paste the QR code onto the canvas
        box = (0, 0, qrcode_img.size[0], qrcode_img.size[1])  # Ensure the sizes match
        canvas.paste(qrcode_img, box)

        # Save the canvas to a buffer
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        buffer.seek(0)

        # Generate a file name for the QR code
        fname = f'qr_code-{dpi_instance.id.NSS}.png'

        # Save the QR code to the model instance
        dpi_instance.qr_code.save(fname, File(buffer), save=False)

        # Clean up
        buffer.close()
        canvas.close()

        # Return the model instance
        return dpi_instance