import { Component, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { AuthService } from '../../services/authservice.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SharedService } from '../../services/sharedservice.service';
import { Router } from '@angular/router';
import { BarcodeFormat } from '@zxing/browser';
import { ZXingScannerModule } from '@zxing/ngx-scanner'; // Import du module ZXingScannerModule

@Component({
  selector: 'app-rechercher-patient',
  standalone: true,
  imports: [CommonModule, FormsModule, ZXingScannerModule], // Ajout du ZXingScannerModule
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  templateUrl: './rechercher-patient.component.html',
  styleUrls: ['./rechercher-patient.component.css'],
})
export class RechercherPatientComponent {
  nss: string = ''; // Lier ce champ à l'input du NSS
  patient: any = null; // Stocke les données du patient
  errorMessage: string = ''; // Gère les messages d'erreur
  isScanning: boolean = false; // Indique si le scanner QR est actif
  torchEnabled: boolean = false; // Active/Désactive le flash de la caméra
  allowedFormats = [BarcodeFormat.QR_CODE]; // Formats autorisés
  scannerEnabled: boolean = false; // Pour vérifier si le scanner est bien initialisé

  constructor(
    private authService: AuthService,
    private sharedService: SharedService,
    private router: Router
  ) {}

  // Méthode pour rechercher un patient par NSS
  onSearchPatient(): void {
    if (this.nss.trim() === '') {
      this.errorMessage = 'Le NSS est requis.';
      this.patient = null;
      return;
    }

    this.authService.getPatientByNSS(this.nss).subscribe({
      next: (response: any) => {
        if (response && response[0]) {
          this.patient = response[0];
          this.errorMessage = '';
          this.getPatientDetails(this.patient.id);
          this.sharedService.updatePatientId(this.patient.id);
        } else {
          this.errorMessage = 'Aucun patient trouvé pour ce NSS.';
          this.patient = null;
        }
      },
      error: (err) => {
        console.error('Erreur lors de la recherche :', err);
        this.errorMessage = 'Une erreur est survenue lors de la recherche.';
        this.patient = null;
      },
    });
  }

  // Méthode pour récupérer les détails du patient par ID
  getPatientDetails(id: number): void {
    this.authService.getPatientById(id).subscribe({
      next: (response: any) => {
        if (response) {
          this.patient = response;
          console.log('Détails du patient récupérés:', this.patient);
        } else {
          this.errorMessage = 'Aucun détail trouvé pour ce patient.';
        }
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des détails du patient :', err);
        this.errorMessage = 'Une erreur est survenue lors de la récupération des détails.';
      },
    });
  }

  // Navigation vers la page DPI
  goToDpiPage(): void {
    this.router.navigate(['/patient']);
  }

  // Ouvrir le scanner QR
  openScanner(): void {
    this.isScanning = true;
  }

  // Fermer le scanner QR
  closeScanner(): void {
    this.isScanning = false;
  }

  // Activer/Désactiver le flash
  toggleTorch(): void {
    this.torchEnabled = !this.torchEnabled;
  }

  // Gestion de l'événement de résultat du QR Code scanné
  handleQrCodeResult(event: any): void {
    const qrCodeResult: string = event?.text || '';
    console.log('QR Code scanné :', qrCodeResult);
    if (qrCodeResult) {
      this.nss = qrCodeResult; // Mettre à jour le NSS avec le résultat du QR Code
      this.isScanning = false; // Arrêter le scan après un résultat
    }
  }

  // Démarrer le scan
  startScanning(): void {
    this.isScanning = true;
  }

  // Arrêter le scan
  stopScanning(): void {
    this.isScanning = false;
  }
}
