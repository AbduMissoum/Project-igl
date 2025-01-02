// rechercher-patient.component.ts
import { Component } from '@angular/core';
import { AuthService } from '../../services/authservice.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PatientService } from '../../services/patient.service'; 
import { SharedService } from '../../services/sharedservice.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-rechercher-patient',
  imports : [FormsModule , CommonModule ],
  templateUrl: './rechercher-patient.component.html',
  styleUrls: ['./rechercher-patient.component.css']
})
export class RechercherPatientComponent {
  nss: string = ''; // Lier ce champ à l'input du NSS
  patient: any = null; // Stocke les données du patient
  errorMessage: string = ''; // Gère les messages d'erreur

  

  constructor(private authService: AuthService , private sharedService: SharedService , private router : Router) {}

  // Méthode pour rechercher un patient par NSS
  onSearchPatient(): void {
    if (this.nss.trim() === '') {
      this.errorMessage = 'Le NSS est requis.';
      this.patient = null;
      return;
    }
    
    

    // Appel au service pour obtenir les informations du patient
    this.authService.getPatientByNSS(this.nss).subscribe({     
      next: (response: any) => {
        if (response  ) {
          console.log(response);
          this.patient = response[0]; 

          console.log(this.patient);
          console.log(this.patient.id);
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
      }
    });
    
  }
  getPatientDetails(id: number): void {
    this.authService.getPatientById(id).subscribe({
      next: (response: any) => {
        if (response) {
          this.patient = response;  // Mettez à jour les données du patient
          console.log('Détails du patient récupérés:', this.patient);
        } else {
          this.errorMessage = 'Aucun détail trouvé pour ce patient.';
        }
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des détails du patient :', err);
        this.errorMessage = 'Une erreur est survenue lors de la récupération des détails.';
      }
    });
  }
  rechercherPatient(): void {
    // Logique pour obtenir l'ID du patient via NSS
    const patientId = 5; // Exemple : remplacez par l'ID réel après la recherche
    this.sharedService.updatePatientId(patientId);
  }
  goToDpiPage(): void {
    this.router.navigate(['/patient']);
  }
}