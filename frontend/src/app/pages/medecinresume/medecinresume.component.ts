import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { SharedService } from '../../services/sharedservice.service';
import { FormsModule } from '@angular/forms';
import { ConsultationService } from '../../services/consultation.service';

@Component({
  selector: 'app-medecinresume',
  imports: [CommonModule , FormsModule],
  templateUrl: './medecinresume.component.html',
  styleUrl: './medecinresume.component.css'
})
export class MedecinresumeComponent implements OnInit {
  consultationDetails: any;
  resumeText: string = '';

  constructor(private sharedService: SharedService , private consultationService : ConsultationService) {}

  ngOnInit(): void {
    // Récupérer les détails de la consultation depuis SharedService
    this.sharedService.consultationDetails$.subscribe((data) => {
      this.consultationDetails = data;
      console.log('Détails de la consultation dans ResumeComponent :', this.consultationDetails);
      this.resumeText = data?.resume || ''; 
    });
  }
  saveResume(): void {
    this.resumeText = this.consultationDetails.resume;
    if (this.consultationDetails && this.resumeText !== '') {
      this.consultationService.updateConsultationResume(this.consultationDetails.id, this.resumeText)
        .subscribe({
          next: (response) => {
            console.log('Résumé mis à jour avec succès:', response);
            // Affichage d'un message ou d'une alerte si nécessaire
          },
          error: (err) => {
            console.error('Erreur lors de la mise à jour du résumé:', err);
          }
        });
    }
  }
}


