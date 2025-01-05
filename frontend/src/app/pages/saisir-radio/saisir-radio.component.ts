import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from '../../services/authservice.service';
import { CommonModule } from '@angular/common';
import Swal from 'sweetalert2';

@Component({
  imports: [FormsModule, CommonModule],
  selector: 'app-saisir-radio',
  templateUrl: './saisir-radio.component.html',
  styleUrls: ['./saisir-radio.component.css']
})
export class SaisirRadioComponent implements OnInit {
  compteRendu: string = ''; // Contenu du compte rendu
  selectedFile: File | null = null; // Fichier de l'examen image
  radioid: string = ''; // ID du bilan (extraction de l'URL)
  isLoading: boolean = false; // Indicateur de chargement

  // Style mémorisé pour les alertes SweetAlert2
  swalOptions = {
    customClass: {
      popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Style du popup
      title: 'text-2xl font-bold text-fonce', // Style du titre
      confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Style du bouton de confirmation
      cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]', // Style du bouton d'annulation
    },
  };

  constructor(
    private activatedRoute: ActivatedRoute,
    private authService: AuthService,
    private http: HttpClient
  ) {
    // Récupération de l'ID du bilan à partir de l'URL
    this.activatedRoute.params.subscribe(params => {
      this.radioid = params['radioid']; // Assurez-vous que 'radioid' est bien présent dans l'URL
    });
  }

  ngOnInit(): void {
    this.fetchBilanDetails(); // Récupérer les détails initiaux du bilan
  }

  // Récupération des détails du bilan
  fetchBilanDetails(): void {
    if (!this.radioid) {
      Swal.fire({
        title: 'Erreur',
        text: 'ID du bilan manquant.',
        icon: 'error',
        ...this.swalOptions // Appliquer le style mémorisé
      });
      return;
    }

    this.isLoading = true;

    // Ajouter le token d'authentification dans les en-têtes
    const token = this.authService.getToken();
    if (!token) {
      Swal.fire({
        title: 'Erreur',
        text: 'Token d\'authentification manquant.',
        icon: 'error',
        ...this.swalOptions // Appliquer le style mémorisé
      });
      return;
    }

    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    console.log('fds',this.radioid),

    this.http
      .get<any>(`http://localhost:8000/bilan-radio/voir-bilan/${this.radioid}/`, { headers })
      .subscribe({
        next: (response) => {
          this.isLoading = false;
          console.log('Détails du bilan récupérés :', response);
          this.compteRendu = response.compte_rendu || ''; // Initialiser le compte rendu
          // Gérez d'autres données si nécessaires
        },
        error: (error) => {
          this.isLoading = false;
          Swal.fire({
            title: 'Erreur',
            text: 'Erreur lors de la récupération des détails du bilan.',
            icon: 'error',
            ...this.swalOptions // Appliquer le style mémorisé
          });
          console.error('Erreur GET :', error);
        },
      });
  }

  // Gestion du fichier sélectionné
  onFileSelected(event: any): void {
    const file: File = event.target.files[0];
    if (file) {
      this.selectedFile = file;
    }
  }

  // Soumettre le rapport avec le compte rendu et l'image
  submitReport(): void {
    if (!this.compteRendu) {
      Swal.fire({
        title: 'Erreur',
        text: 'Veuillez saisir le compte rendu.',
        icon: 'error',
        ...this.swalOptions // Appliquer le style mémorisé
      });
      return;
    }

    if (!this.selectedFile) {
      Swal.fire({
        title: 'Erreur',
        text: 'Veuillez télécharger une image.',
        icon: 'error',
        ...this.swalOptions // Appliquer le style mémorisé
      });
      return;
    }

    // Créer le formulaire de données à envoyer (multipart/form-data)
    const formData = new FormData();
    formData.append('compte_rendu', this.compteRendu);
    formData.append('examen_image', this.selectedFile, this.selectedFile.name);

    // Ajouter le token d'authentification dans l'en-tête
    const token = this.authService.getToken();
    if (!token) {
      Swal.fire({
        title: 'Erreur',
        text: 'Token d\'authentification manquant.',
        icon: 'error',
        ...this.swalOptions // Appliquer le style mémorisé
      });
      return;
    }

    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

    this.http
      .patch(
        `http://localhost:8000/bilan-radio/remplir/${this.radioid}/`,
        formData,
        { headers }
      )
      .subscribe({
        next: (response) => {
          Swal.fire({
            title: 'Succès',
            text: 'Bilan mis à jour avec succès!',
            icon: 'success',
            ...this.swalOptions // Appliquer le style mémorisé
          });
          console.log('Réponse PATCH :', response);
        },
        error: (error) => {
          Swal.fire({
            title: 'Erreur',
            text: 'Une erreur est survenue lors de la mise à jour du bilan.',
            icon: 'error',
            ...this.swalOptions // Appliquer le style mémorisé
          });
          console.error('Erreur PATCH :', error);
        },
      });
  }
}
