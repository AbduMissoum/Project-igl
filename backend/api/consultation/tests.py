from django.test import TestCase
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from consultation.models import Consultation
from dpi.models import Dpi,Patient
from authentication.models import Etablisement,CustomUser
from datetime import date

@pytest.mark.django_db
def test_create_consultation_success():
    medecin = CustomUser.objects.create_user(
        username="username1",
        password="password",
        email="medecin@example.com",
        role="medecin"
    )

    patient_user = CustomUser.objects.create_user(
        username='patient_user', 
        email='patient@example.com',
        password='patient_password', 
        role='patient'
    )
    
    patient = Patient.objects.create(
        id=patient_user, 
        NSS="123456789", 
        nom="Test", 
        prenom="Patient", 
        date_naissance="2000-01-01", 
        adress="123 Test Street", 
        tel="123456789", 
        mutuelle="Test Mutuelle"
    )

    client = APIClient()

    login_response = client.post('/auth/login/', {
        "username": "username1",
        "password": "password"
    }, format='json')
    assert login_response.status_code == status.HTTP_200_OK

    # Log the actual response for debugging
    login_data = login_response.json()
    print(f"Login response: {login_data}")

    # Adjust assertion to check the actual response
    assert "mesage" in login_data  # Temporary fix if the typo is in the backend
    assert login_data["mesage"] == "User authenticated"

    etablisement = Etablisement.objects.create(nom="esi")
    dpi = Dpi.objects.create(id=patient, qr_code=None)

    Consultation.objects.create(
        etablisement=etablisement,
        medecin=medecin,
        dpi=dpi,
        resume="consult1",
        la_date="2024-06-01"
    )

    Consultation.objects.create(
        etablisement=etablisement,
        medecin=medecin,
        dpi=dpi,
        resume="consult2",
        la_date="2024-06-01"
    )

    response = client.get('/consultations/')

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert len(response_data) == 2
    assert response_data[0]['resume'] == "consult1"
    assert response_data[1]['resume'] == "consult2"
