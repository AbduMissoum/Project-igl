import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { SharedService } from '../../services/sharedservice.service';
import { AuthService } from '../../services/authservice.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-medecinbilanradio',
  imports: [CommonModule, FormsModule],
  templateUrl: './medecinbilanradio.component.html',
  styleUrls: ['./medecinbilanradio.component.css']
})
export class MedecinbilanradioComponent implements OnInit {
  title = 'Bilan Radiologique';
  radioName: string = '';
  isPopupVisible: boolean = false;
  consultationDetails: any;
  examenImage: string | null = null;
  compteRendu: string | null = null;

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
    private authService: AuthService,
    private sharedService: SharedService
  ) {}

  ngOnInit(): void {
    // Récupérer les détails de la consultation via SharedService
    this.sharedService.consultationDetails$.subscribe((data) => {
      this.consultationDetails = data;
   
      console.log('Détails de la consultation dans Medecinbilanradio:', this.consultationDetails);
      if (this.consultationDetails?.id) {
        this.loadBilanData(this.consultationDetails.id);
      }
    });
  }

  openPopup(): void {
    this.isPopupVisible = true;
  }

  closePopup(): void {
    this.isPopupVisible = false;
  }

  submitRequest(): void {
    if (!this.consultationDetails || !this.consultationDetails.id) {
      console.error('ID de consultation manquante');
      Swal.fire({
        title: 'Erreur',
        text: 'ID de consultation manquante',
        icon: 'error',
        ...this.swalOptions
      });
      return;
    }

    if (!this.radioName) {
      console.error('Le type du Radio est manquant');
      Swal.fire({
        title: 'Erreur',
        text: 'Le type du Radio est manquant',
        icon: 'error',
        ...this.swalOptions
      });
      return;
    }

    const requestData = {
      consultation_id: this.consultationDetails.id,
      type: this.radioName,
    };

    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + this.authService.getToken(),
    });

    this.http.post('http://localhost:8000/bilan-radio/demande', requestData, { headers }).subscribe({
      next: (response: any) => {
        console.log('Réponse de l\'API:', response);
        this.isPopupVisible = false; // Fermer le pop-up après soumission
        Swal.fire({
          title: 'Succès',
          text: 'Demande envoyée avec succès.',
          icon: 'success',
          ...this.swalOptions
        });
      },
      error: (error) => {
        console.error('Erreur lors de la demande:', error);
        Swal.fire({
          title: 'Erreur',
          text: 'Erreur lors de la demande. Veuillez vérifier les informations et réessayer.',
          icon: 'error',
          ...this.swalOptions
        });
      }
    });
  }

  loadBilanData(consultationId: number): void {
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + this.authService.getToken(),
    });

    this.http
      .get(`http://localhost:8000/bilan-radio/bilan-details/${consultationId}/`, { headers })
      .subscribe({
        next: (response: any) => {
          console.log('Données de l\'examen:', response);
          this.compteRendu = response?.message.bilan?.compte_rendu || 'Aucun compte rendu disponible.';
          this.examenImage = `http://localhost:8000${response?.message.examen_image }` || null;
        },
        error: (err) => {
          console.error('Erreur lors de la récupération des données:', err);
        },
      });
  }
}
