import { Component , OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import {  RouterLink , Router } from '@angular/router';
import { SharedService } from '../../services/sharedservice.service';
import { ConsultationService } from '../../services/consultation.service';


interface Historique {
  id : number;
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
export class MedecinHistoriqueConsultationComponent implements OnInit {
  historiques: Historique[] = [ ];

  // Variables pour gérer le modal et les données de la consultation
  isModalOpen: boolean = false;
  newConsultation: { medecin: string, etablisement: string, date: string, heure: string } = { medecin: '', etablisement: '', date: '', heure: '' };


  constructor(
    private sharedService: SharedService,   // Injection du SharedService
    private consultationService: ConsultationService ,// Injection du service de création de consultation
    private router: Router
  ) {}
  ngOnInit(): void {
    // Récupérer l'ID du patient et les consultations associées
    this.sharedService.patientId$.subscribe(patientId => {
      if (patientId !== null) {
        this.consultationService.getConsultationsByDpi(patientId).subscribe({
          next: (data) => {
            this.historiques = data.map((item: any) => ({
              id : item.id,
              medecin: item.medecin.username, // Nom du médecin
              etablissement: item.etablisement, // Établissement
              date: new Date(item.la_date), // Date de la consultation
              heure: '10:00' // Heure statique (par défaut)
            }));
          },
          error: (err) => {
            console.error('Erreur lors de la récupération des consultations :', err);
          }
        });
      } else {
        console.error('Aucun patient ID trouvé.');
      }
    });
  }

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
                id : 9,
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
  
  viewDetails(consultationId: number): void {
    this.consultationService.getConsultationDetailsById(consultationId).subscribe({
      next: (data) => {
        // 'data' contient les détails de la consultation
        console.log('Détails de la consultation récupérés :', data);
        
        // Partager les détails avec un composant enfant via un service (SharedService)
        this.sharedService.setConsultationDetails(data);  // Par exemple, avec SharedService

        // Optionnel : rediriger vers une page dédiée ou afficher les détails dans une modal
        this.router.navigate(['/medecin', consultationId]); // Par exemple, rediriger vers /medecin/{id}
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des détails :', err);
      }
    });
  }  
  

}