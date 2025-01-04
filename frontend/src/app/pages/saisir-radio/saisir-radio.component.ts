import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from '../../services/authservice.service';
import { CommonModule } from '@angular/common';

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
      alert('ID du bilan manquant.');
      return;
    }

    this.isLoading = true;

    // Ajouter le token d'authentification dans les en-têtes
    const token = this.authService.getToken();
    if (!token) {
      alert('Token d\'authentification manquant.');
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
          alert('Erreur lors de la récupération des détails du bilan.');
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
      alert('Veuillez saisir le compte rendu.');
      return;
    }

    if (!this.selectedFile) {
      alert('Veuillez télécharger une image.');
      return;
    }

    // Créer le formulaire de données à envoyer (multipart/form-data)
    const formData = new FormData();
    formData.append('compte_rendu', this.compteRendu);
    formData.append('examen_image', this.selectedFile, this.selectedFile.name);

    // Ajouter le token d'authentification dans l'en-tête
    const token = this.authService.getToken();
    if (!token) {
      alert('Token d\'authentification manquant.');
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
          alert('Bilan mis à jour avec succès!');
          console.log('Réponse PATCH :', response);
        },
        error: (error) => {
          alert('Une erreur est survenue lors de la mise à jour du bilan.');
          console.error('Erreur PATCH :', error);
        },
      });
  }
}
