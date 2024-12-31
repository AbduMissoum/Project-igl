import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {  RouterLink } from '@angular/router';
import { SharedService } from '../../services/sharedservice.service';
import { ConsultationService } from '../../services/consultation.service';


interface Historique {
  medecin: string;
  etablissement: string;
  date: Date;
  heure: string;
}

@Component({
  selector: 'app-medecin-historique-consultation',
  standalone: true,
  imports: [CommonModule , FormsModule , RouterLink , ],
  templateUrl: './medecin-historique-consultation.component.html',
  styleUrls: ['./medecin-historique-consultation.component.css']
})
// export class MedecinHistoriqueConsultationComponent {
//   historiques: Historique[] = [
//     { medecin: 'Dr. Dupont', etablissement: 'Clinique Saint-Martin', date: new Date('2024-12-20'), heure: '10:30' },
//     { medecin: 'Dr. Lefevre', etablissement: 'Hôpital Central', date: new Date('2024-12-22'), heure: '14:00' },
//     { medecin: 'Dr. Bernard', etablissement: 'Centre Médical Nord', date: new Date('2024-12-23'), heure: '09:15' },
//     { medecin: 'Dr. Martin', etablissement: 'Polyclinique Sud', date: new Date('2024-12-24'), heure: '16:45' }
//   ];

//   // Variable pour gérer l'ouverture/fermeture du modal
//   isModalOpen: boolean = false;

//   // Modèle pour la nouvelle consultation
//   newConsultation: Historique = { medecin: '', etablissement: '', date: new Date(), heure: '' };

//   constructor() {}

//   ngOnInit(): void {
//     console.log('Component initialized');
//   }

//   openModal(): void {
//     this.isModalOpen = true;
//   }

//   closeModal(): void {
//     this.isModalOpen = false;
//   }

//   addConsultation(): void {
//     if (this.newConsultation.medecin && this.newConsultation.etablissement && this.newConsultation.date && this.newConsultation.heure) {
//       // Ajouter la nouvelle consultation à la liste
//       this.historiques.push({
//         ...this.newConsultation,
//         date: new Date(this.newConsultation.date) // S'assurer que la date est correctement formatée
//       });

//       // Réinitialiser le formulaire
//       this.newConsultation = { medecin: '', etablissement: '', date: new Date(), heure: '' };
//       this.closeModal();
//     }
//   }
// }
export class MedecinHistoriqueConsultationComponent {
  historiques: Historique[] = [
    { medecin: 'Dr. Dupont', etablissement: 'Clinique Saint-Martin', date: new Date('2024-12-20'), heure: '10:30' },
    { medecin: 'Dr. Lefevre', etablissement: 'Hôpital Central', date: new Date('2024-12-22'), heure: '14:00' },
    { medecin: 'Dr. Bernard', etablissement: 'Centre Médical Nord', date: new Date('2024-12-23'), heure: '09:15' },
    { medecin: 'Dr. Martin', etablissement: 'Polyclinique Sud', date: new Date('2024-12-24'), heure: '16:45' }
  ];

  // Variables pour gérer le modal et les données de la consultation
  isModalOpen: boolean = false;
  newConsultation: { medecin: string, etablisement: string, date: string, heure: string } = { medecin: '', etablisement: '', date: '', heure: '' };

  constructor(
    private sharedService: SharedService,   // Injection du SharedService
    private consultationService: ConsultationService // Injection du service de création de consultation
  ) {}

  openModal(): void {
    this.isModalOpen = true;
  }

  closeModal(): void {
    this.isModalOpen = false;
  }

  // Fonction pour ajouter une consultation
  addConsultation(): void {
    if (this.newConsultation.medecin && this.newConsultation.etablisement && this.newConsultation.date && this.newConsultation.heure) {
      this.sharedService.patientId$.subscribe(patientId => {
        if (patientId !== null) {
          // Appel à l'API pour créer la consultation
          this.consultationService.createConsultation(this.newConsultation.etablisement, patientId, this.newConsultation.date).subscribe({
            next: (response) => {
              console.log('Consultation ajoutée avec succès:', response);
              // Ajouter la consultation à l'historique
              this.historiques.push({
                medecin: this.newConsultation.medecin,
                etablissement: this.newConsultation.etablisement,
                date: new Date(this.newConsultation.date),
                heure: this.newConsultation.heure
              });
              // Réinitialiser le formulaire et fermer le modal
              this.newConsultation = { medecin: '', etablisement: '', date: '', heure: '' };
              this.closeModal();
            },
            error: (err) => {
              console.error('Erreur lors de la création de la consultation:', err);
            }
          });
        } else {
          console.error('Aucun patient ID trouvé.');
        }
      });
    }
  }
}