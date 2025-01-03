import pytest
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import CustomUser
from les_soins.models import Soins
from dpi.models import Patient
from django.utils.timezone import now

@pytest.mark.django_db
def test_soins_list_by_patient_id():
    # Step 1: Create a CustomUser (patient)
    patient_user = CustomUser.objects.create_user(
        username='patient_user', 
        email='patient@example.com',
        password='patient_password', 
        role='patient'
    )
    
    # Create patient with correct foreign key relationship
    patient = Patient.objects.create(
        id=patient_user,  # Changed from id=patient_user to user=patient_user
        NSS="123456789", 
        nom="Test", 
        prenom="Patient", 
        date_naissance="2000-01-01", 
        adress="123 Test Street", 
        tel="123456789", 
        mutuelle="Test Mutuelle"
    )

    # Step 2: Create another user (infirmier)
    infirmier_user = CustomUser.objects.create_user(
        username='infirmier_user', 
        email='infirmier@example.com',
        password='infirmier_password', 
        role='infirmier'
    )

    # Step 3: Authentication setup
    client = APIClient()
    # Use the actual login endpoint since session authentication is being used
    login_response = client.post('/auth/login/', {
        "username": "patient_user",
        "password": "patient_password"
    }, format='json')
    assert login_response.status_code == status.HTTP_200_OK
    assert "mesage" in login_response.json()
    assert login_response.json()["mesage"] == "User authenticated"

    # Step 4: Create some soins for the patient
    Soins.objects.create(
        description="Soin 1",
        patient=patient,
        infirmier=infirmier_user,
        la_date=now().date()
    )
    Soins.objects.create(
        description="Soin 2",
        patient=patient,
        infirmier=infirmier_user,
        la_date=now().date()
    )

    # Step 5: Call the soins_list_by_patient_id view
    # Using the correct full URL path including the soins/ prefix
    response = client.get(f'/soins/patient/{patient.id.id}/')

    # Step 6: Print debug information
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")
    
    # Step 7: Validate the response
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()  # Convert response content to JSON
    assert len(response_data) == 2  # Two soins created
    assert response_data[0]['description'] == "Soin 1"
    assert response_data[1]['description'] == "Soin 2"