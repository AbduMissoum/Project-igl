import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { ConsultationService } from '../../services/consultation.service';
import { FormsModule } from '@angular/forms';
import { SharedService } from '../../services/sharedservice.service';

interface Historique {
  id: number;
  medecin: string;
  etablissement: string;
  date: Date;
  heure: string;
}

@Component({
  selector: 'app-patient-consultation-historique',
  imports: [CommonModule , FormsModule],
  templateUrl: './patient-consultation-historique.component.html',
  styleUrls: ['./patient-consultation-historique.component.css']
})
export class PatientConsultationHistoriqueComponent implements OnInit {
  historiques: Historique[] = [];

  constructor(
    private sharedService : SharedService,
    private consultationService: ConsultationService, // Injection du service de création de consultation
    private router: Router
  ) {}

  ngOnInit(): void {
    // Récupérer l'ID du patient depuis le localStorage
    const patientIdString = localStorage.getItem('patient_id');
    if (patientIdString) {
      const patientId = parseInt(patientIdString, 10);
      if (!isNaN(patientId)) {
        console.log(patientId);
        // Appeler le service pour récupérer les consultations
        this.consultationService.getConsultationsByDpi(patientId).subscribe({
          next: (data) => {
            this.historiques = data.map((item: any) => ({
              id: item.id,
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
        console.error("L'ID du patient n'est pas un entier valide.");
      }
    } else {
      console.error('Aucun ID du patient trouvé dans le localStorage.');
    }
  }

  viewDetails(consultationId: number): void {
    this.consultationService.getConsultationDetailsById(consultationId).subscribe({
      next: (data) => {
        console.log('Détails de la consultation récupérés :', data);

        // Sauvegarder les détails de la consultation dans le SharedService
        this.sharedService.setConsultationDetails(data);

        // Rediriger vers la page dédiée
        this.router.navigate(['/patientcons', consultationId]);
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des détails :', err);
      }
    });
  }
}
