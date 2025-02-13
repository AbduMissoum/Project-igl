import { Component, OnInit } from '@angular/core';
import { SharedService } from '../../services/sharedservice.service';
import { ConsultationService } from '../../services/consultation.service';
import Swal from 'sweetalert2';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-resume',
  standalone: true,
  templateUrl: './resume.component.html',
  imports : [FormsModule , CommonModule],
  styleUrls: ['./resume.component.css']
})
export class ResumeComponent implements OnInit {
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
 
  //  saveResume(): void {
  //    if (this.consultationDetails && this.resumeText !== '') {
  //      // Afficher le pop-up de confirmation
  //      Swal.fire({
  //        title: 'Êtes-vous sûr ?',
  //        text: "Vous êtes sur le point de sauvegarder le résumé de la consultation.",
  //        icon: 'warning',
  //        showCancelButton: true,
  //        confirmButtonColor: '#5DA5B9',
  //        cancelButtonColor: '#D3E7E8',
  //        confirmButtonText: 'Oui, sauvegarder',
  //        cancelButtonText: 'Annuler',
  //      }).then((result) => {
  //        if (result.isConfirmed) {
  //          // Soumettre la mise à jour du résumé
  //          this.consultationService.updateConsultationResume(this.consultationDetails.id, this.resumeText)
  //            .subscribe({
  //              next: (response) => {
  //                console.log('Résumé mis à jour avec succès:', response);
  //                Swal.fire('Succès', 'Le résumé a été sauvegardé avec succès.', 'success');
  //              },
  //              error: (err) => {
  //                console.error('Erreur lors de la mise à jour du résumé:', err);
  //                Swal.fire('Erreur', 'Une erreur est survenue lors de la mise à jour du résumé.', 'error');
  //              }
  //            });
  //        }
  //      });
  //    } else {
  //      Swal.fire('Attention', 'Le résumé est vide, veuillez ajouter un résumé.', 'warning');
  //    }
  //  }
 }
 