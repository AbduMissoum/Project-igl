

  import { Component, OnInit } from '@angular/core';
  import { HttpClient, HttpHeaders } from '@angular/common/http';
  import { SharedService } from '../../services/sharedservice.service';
  import { AuthService } from '../../services/authservice.service';
  import Swal from 'sweetalert2';
  import { CommonModule } from '@angular/common';
  import { FormsModule } from '@angular/forms';
  
  
  @Component({
    selector: 'app-ordonance',
    standalone: true,
    imports: [CommonModule, FormsModule],
    templateUrl: './ordonance.component.html',
    styleUrls: ['./ordonance.component.css']
  })
  export class OrdonanceComponent  implements OnInit {
    title = 'Ordonnance';
    consultationId: number = 0; // ID de la consultation
    consultationDetails: any; // Détails de la consultation
    traitements = [
      { la_dose: '', la_durre: '', medicament: { nom: '' } },
    ]; // Liste des traitements
  
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
      private authService: AuthService
    ) {}
  
    ngOnInit(): void {
      // Récupérer les détails de la consultation depuis SharedService
      this.sharedService.consultationDetails$.subscribe((data) => {
        this.consultationDetails = data;
        this.consultationId = data?.id; // Récupérer l'ID de la consultation
        console.log('Détails de la consultation dans OrdonnanceComponent :', this.consultationDetails);
  
        // Récupérer les ordonnances pour cette consultation
        this.getOrdonnancesForConsultation(this.consultationId);
      });
    }
  
  
  
   
    // Méthode pour récupérer les ordonnances de la consultation
    getOrdonnancesForConsultation(consultationId: number): void {
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
  
      this.http.get(`http://localhost:8000/ordonnances/consultation/${consultationId}/`, { headers })
        .subscribe({
          next: (response: any) => {
            if (response && Array.isArray(response)) {
              this.traitements = response.map((ordonnance) => ({
                la_dose: ordonnance.traitements[0]?.la_dose || '',
                la_durre: ordonnance.traitements[0]?.la_durre || '',
                medicament: { nom: ordonnance.traitements[0]?.medicament?.nom || '' },
              }));
            }
          },
          error: (error) => {
            Swal.fire({
              title: 'Erreur',
              text: 'Impossible de récupérer les ordonnances.',
              icon: 'error',
              ...this.swalOptions,
            });
            console.error('Erreur GET :', error);
          },
        });
    }
  }
  
