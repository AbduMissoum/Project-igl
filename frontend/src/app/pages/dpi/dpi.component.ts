import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { QRCodeComponent } from 'angularx-qrcode';
import { AuthService } from '../../services/authservice.service';

@Component({
 
  standalone: true, // Ce composant est Standalone
  imports: [CommonModule, QRCodeComponent],
 
    selector: 'app-dpi',

    templateUrl: './dpi.component.html',
    styleUrl: './dpi.component.css'
  })
  export class DpiComponent  implements OnInit {
  nss: string = ''; // Initialisation du NSS
  patientData: any = null; // Stocke les données du patient
  qrCodeData: string = ''; // Données pour le QR Code
  patientId: number | null = null; // ID du patient

  constructor(private patientService: AuthService) {}

  ngOnInit(): void {
    // Récupération du patientId depuis le localStorage
    const patientIdString = localStorage.getItem('patient_id');
    if (patientIdString) {
      const patientId = parseInt(patientIdString, 10);
      if (!isNaN(patientId)) {
        this.patientId = patientId;
        this.loadPatientData(); // Charger les données du patient
      } else {
        console.error("L'ID du patient n'est pas un entier valide.");
      }
    } else {
      console.error('Aucun ID du patient trouvé dans le localStorage.');
    }
  }

  loadPatientData(): void {
    if (!this.patientId) return;

    this.patientService.getPatientById(this.patientId).subscribe({
      next: (response) => {
        this.patientData = response;
        this.nss = this.patientData?.NSS || ''; // NSS du patient
        this.qrCodeData = this.nss; // Utiliser le NSS comme données du QR Code
      },
      error: (err) => {
        console.error('Erreur lors du chargement des données du patient :', err);
        this.patientData = null;
      }
    });
  }
}


