import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { SharedService } from '../../services/sharedservice.service';
import { ConsultationService } from '../../services/consultation.service';
import { AuthService } from '../../services/authservice.service';
import Swal from 'sweetalert2';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-medecinordonance',
  imports: [CommonModule , FormsModule],
  templateUrl: './medecinordonance.component.html',
  styleUrls: ['./medecinordonance.component.css']
})
export class MedecinordonanceComponent implements OnInit {
  title = 'Ordonnance';
  consultationId: number = 0;  // ID de la consultation
  consultationDetails: any;  // Détails de la consultation
  traitements = [{ la_dose: '', la_durre: '', medicament: { nom: '' } }]; // Liste des traitements

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
    private http: HttpClient,
    private sharedService: SharedService,
    private authService: AuthService,
    private consultationService: ConsultationService
  ) {}

  ngOnInit(): void {
    // Récupérer les détails de la consultation depuis SharedService
    this.sharedService.consultationDetails$.subscribe((data) => {
      this.consultationDetails = data;
      this.consultationId = data?.id; // Récupérer l'ID de la consultation
      console.log('Détails de la consultation dans OrdonnanceComponent :', this.consultationDetails);
    });
  }

  // Ajouter un traitement vide
  addTreatment(): void {
    this.traitements.push({ la_dose: '', la_durre: '', medicament: { nom: '' } });
  }

  // Supprimer un traitement
  removeTreatment(index: number): void {
    this.traitements.splice(index, 1);
  }

  // Soumettre l'ordonnance
  submit(): void {
    if (this.traitements.some(t => !t.la_dose || !t.la_durre || !t.medicament.nom)) {
      Swal.fire({
        title: 'Erreur',
        text: 'Tous les champs doivent être remplis.',
        icon: 'error',
        ...this.swalOptions,
      });
      return;
    }
    console.log(this.consultationId);

    // Créer le corps de la requête
    const data = {
      consultation: this.consultationId,
      traitements: this.traitements,
    };

    // Récupérer le token d'authentification
    const token = this.authService.getToken();
    if (!token) {
      Swal.fire({
        title: 'Erreur',
        text: 'Token d\'authentification manquant.',
        icon: 'error',
        ...this.swalOptions,
      });
      return;
    }

    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

    // Envoyer la requête POST
    this.http.post('http://localhost:8000/ordonnances/', data, { headers })
      .subscribe({
        next: (response) => {
          Swal.fire({
            title: 'Succès',
            text: 'Ordonnance créée avec succès!',
            icon: 'success',
            ...this.swalOptions,
          });
          console.log('Réponse POST :', response);
        },
        error: (error) => {
          Swal.fire({
            title: 'Erreur',
            text: 'Une erreur est survenue lors de la création de l\'ordonnance.',
            icon: 'error',
            ...this.swalOptions,
          });
          console.error('Erreur POST :', error);
        }
      });
  }
}
