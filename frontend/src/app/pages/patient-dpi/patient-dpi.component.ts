import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { QRCodeComponent } from 'angularx-qrcode';
import { PatientService } from '../../services/patient.service';
import { AuthService } from '../../services/authservice.service';
import { SharedService } from '../../services/sharedservice.service';

@Component({
  selector: 'app-patient-dpi',
  standalone: true,  // Ce composant est Standalone
  imports: [ CommonModule , QRCodeComponent  ],
  templateUrl: './patient-dpi.component.html',
  styleUrl: './patient-dpi.component.css'
})
export class PatientDPIComponent implements OnInit {
  nss : string = 'ghjklkjhg'
  patientData: any = null; // Stocke les données du patient
  qrCodeData: string = ''; // Données pour le QR Code
  patientId: number = 5; // Exemple d'ID de patient

  constructor(private patientService: AuthService , private sharedService: SharedService) {}

  ngOnInit(): void {
    this.sharedService.patientId$.subscribe((id: number | null) => {
      if (id !== null) {
        this.patientId = id;
        this.loadPatientData();
      }
    });
  }

  loadPatientData(): void {
    if (!this.patientId) return;
  
    this.patientService.getPatientById(this.patientId).subscribe({
      next: (response) => {
        this.patientData = response;
        this.qrCodeData = this.patientData?.NSS || '';
      },
      error: (err) => {
        console.error('Erreur lors du chargement des données du patient :', err);
        this.patientData = null;
      }
    });
}
}


