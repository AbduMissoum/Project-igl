import { CommonModule } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { AuthService } from '../../services/authservice.service';
import { SharedService } from '../../services/sharedservice.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-bilanbio',
  standalone: true,
  templateUrl: './bilanbio.component.html',
  imports: [CommonModule],
  styleUrls: ['./bilanbio.component.css']
})
export class BilanbioComponent {
  title: string = 'Bilan Médical';
   isPopupOpen: boolean = false;
   requestedTests: string[] = []; // Liste des tests demandés
   nss: string = ''; // NSS du patient
   laborantin: string = ''; // Nom du laborantin
   bioResults = [
     { test: '', value:  2, unit: '', reference: '' },
   ];
 
   consultationDetails: any = null;
   private consultationSubscription: Subscription | null = null;
 
   constructor(
     private http: HttpClient,
     private authService: AuthService,
     private sharedService: SharedService
   ) {}
 
   ngOnInit() {
     console.log('mkach id1');
     this.consultationSubscription = this.sharedService.consultationDetails$.subscribe((details) => {
       this.consultationDetails = details;
       console.log('mkach id2');
       if (this.consultationDetails && this.consultationDetails.id) {
         console.log(this.consultationDetails.id);
         this.fetchBilanBiologique(this.consultationDetails.id);
       } else {
         console.error('Consultation details are missing or invalid');
       }
     });
   }
   
   fetchBilanBiologique(consultationId: number): void {
     console.log('ih', consultationId);
     const headers = new HttpHeaders({
       Authorization: 'Bearer ' + this.authService.getToken(),
     });
     
     this.http
       .get(`http://localhost:8000/bilan-bio/details-bilan/${consultationId}/`, { headers })
       .subscribe({
         next: (response: any) => {
           console.log('ih3', response);
           this.bioResults = response.map((param: any) => ({
             test: param.parametre || 'Inconnu',
             value: param.valeur || 'Non disponible',
             unit: param.unite || 'Non spécifié',
             reference: param.valeur_reference || 'Non défini',
           }));
         },
         error: (error) => {
           console.log('ih4', consultationId);
           console.error('Erreur lors de la récupération du bilan biologique :', error);
           alert('Erreur lors de la récupération du bilan biologique.');
         },
       });
   }
 
  
 
   ngOnDestroy() {
     if (this.consultationSubscription) {
       this.consultationSubscription.unsubscribe();
     }
   }
 }
 