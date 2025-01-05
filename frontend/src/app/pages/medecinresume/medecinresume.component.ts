import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { SharedService } from '../../services/sharedservice.service';
import { FormsModule } from '@angular/forms';
import { ConsultationService } from '../../services/consultation.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-medecinresume',
  imports: [CommonModule , FormsModule],
  templateUrl: './medecinresume.component.html',
  styleUrls: ['./medecinresume.component.css']
})
export class MedecinresumeComponent implements OnInit {
  consultationDetails: any;
  resumeText: string = '';

  // Style mémorisé pour les alertes SweetAlert2
  swalOptions = {
    customClass: {
      popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Style du popup
      title: 'text-2xl font-bold text-fonce', // Style du titre
      confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Style du bouton de confirmation
      cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]', // Style du bouton d'annulation
    },
  };

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
    if (this.consultationDetails && this.resumeText !== '') {
      // Afficher le pop-up de confirmation
      Swal.fire({
        title: 'Êtes-vous sûr ?',
        text: "Vous êtes sur le point de sauvegarder le résumé de la consultation.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#5DA5B9',
        cancelButtonColor: '#D3E7E8',
        confirmButtonText: 'Oui, sauvegarder',
        cancelButtonText: 'Annuler',
        ...this.swalOptions // Appliquer le style mémorisé
      }).then((result) => {
        if (result.isConfirmed) {
          // Soumettre la mise à jour du résumé
          this.consultationService.updateConsultationResume(this.consultationDetails.id, this.resumeText)
            .subscribe({
              next: (response) => {
                console.log('Résumé mis à jour avec succès:', response);
                Swal.fire({
                  title: 'Succès',
                  text: 'Le résumé a été sauvegardé avec succès.',
                  icon: 'success',
                  ...this.swalOptions // Appliquer le style mémorisé
                });
              },
              error: (err) => {
                console.error('Erreur lors de la mise à jour du résumé:', err);
                Swal.fire({
                  title: 'Erreur',
                  text: 'Une erreur est survenue lors de la mise à jour du résumé.',
                  icon: 'error',
                  ...this.swalOptions // Appliquer le style mémorisé
                });
              }
            });
        }
      });
    } else {
      Swal.fire({
        title: 'Attention',
        text: 'Le résumé est vide, veuillez ajouter un résumé.',
        icon: 'warning',
        ...this.swalOptions // Appliquer le style mémorisé
      });
    }
  }
}
