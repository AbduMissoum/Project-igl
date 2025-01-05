import { CommonModule } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/authservice.service';
import { SharedService } from '../../services/sharedservice.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-bilanradio',
  standalone: true,
  templateUrl: './bilanradio.component.html',
   imports: [CommonModule],
  styleUrls: ['./bilanradio.component.css']
})
export class BilanradioComponent implements OnInit {
 title = 'Bilan Radiologique';
   radioName: string = '';
   isPopupVisible: boolean = false;
   consultationDetails: any;
   examenImage: string | null = null;
   compteRendu: string | null = null;
 
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
       return;
     }
 
     if (!this.radioName) {
       console.error('Le type du Radio est manquant');
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
         Swal.fire('Succès', 'Demande envoyée avec succès.', 'success');
       },
       error: (error) => {
         console.error('Erreur lors de la demande:', error);
         alert('Erreur lors de la demande. Veuillez vérifier les informations et réessayer.');
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
           console.log('response', response.message.bilan.compte_rendu)
           console.log('response', response.message.examen_image)
           this.compteRendu = response?.message.bilan?.compte_rendu || 'Aucun compte rendu disponible.';
           this.examenImage = `http://localhost:8000${response?.message.examen_image }` || null;
         },
         error: (err) => {
           console.error('Erreur lors de la récupération des données:', err);
           Swal.fire('Erreur', 'Impossible de charger les données de l\'examen.', 'error');
         },
       });
   }
 }
 
