import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SoinsService } from '../../services/soinsService.sevice';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-saisir-soin',
  imports: [FormsModule , CommonModule ],
  templateUrl: './saisir-soin.component.html',
  styleUrls: ['./saisir-soin.component.css']
})
export class SaisirSoinComponent {
  // Style mémorisé pour les alertes SweetAlert2
  swalOptions = {
    customClass: {
      popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Style du popup
      title: 'text-2xl font-bold text-fonce', // Style du titre
      confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Style du bouton de confirmation
      cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]', // Style du bouton d'annulation
    },
  };

  constructor(private soinsService : SoinsService) { }

  onSubmit(): void {
    // Récupération des valeurs des champs
    const nss = (document.getElementById('nss') as HTMLInputElement).value;
    const date = (document.getElementById('date') as HTMLInputElement).value;
    const soins = (document.getElementById('soins') as HTMLTextAreaElement).value;

    // Vérification si les champs sont remplis
    if (!nss) {
      Swal.fire({
        title: 'Erreur',
        text: 'Le champ NSS est requis.',
        icon: 'error',
        ...this.swalOptions
      });
      return;
    }

    if (!date) {
      Swal.fire({
        title: 'Erreur',
        text: 'Le champ date est requis.',
        icon: 'error',
        ...this.swalOptions
      });
      return;
    }

    if (!soins) {
      Swal.fire({
        title: 'Erreur',
        text: 'Le champ description des soins est requis.',
        icon: 'error',
        ...this.swalOptions
      });
      return;
    }

    // Si tous les champs sont remplis, confirmation de soumission
    Swal.fire({
      title: 'Confirmer la soumission',
      text: 'Êtes-vous sûr de vouloir soumettre ce soin?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Oui, soumettre',
      cancelButtonText: 'Annuler',
      ...this.swalOptions
    }).then((result) => {
      if (result.isConfirmed) {
        // Envoi des données si confirmé
        const body = { NSS: nss, la_date: date, description: soins };

        this.soinsService.createSoin(body).subscribe({
          next: (data) => {
            console.log('Soin créé avec succès:', data);
            Swal.fire({
              title: 'Succès',
              text: 'Le soin a été créé avec succès.',
              icon: 'success',
              ...this.swalOptions
            });
          },
          error: (err) => {
            console.error('Erreur lors de la création du soin:', err);
            Swal.fire({
              title: 'Erreur',
              text: 'Une erreur est survenue lors de la création du soin.',
              icon: 'error',
              ...this.swalOptions
            });
          }
        });
      }
    });
  }
}
