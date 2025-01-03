import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { SharedService } from '../../services/sharedservice.service';
import { Subscription } from 'rxjs';
import { AuthService } from '../../services/authservice.service';

@Component({
  selector: 'app-medecinbilanbio',
  imports: [CommonModule, FormsModule],
  templateUrl: './medecinbilanbio.component.html',
  styleUrls: ['./medecinbilanbio.component.css'],
})

export class MedecinbilanbioComponent implements OnInit {
  title: string = 'Bilan Médical';
  isPopupOpen: boolean = false;
  requestedTests: string[] = [];
  nss: string = '';
  laborantin: string = '';

  bioResults = [
    { test: '', value: '', unit: '', reference: '' },
  ];

  // Variable pour stocker les détails de la consultation
  consultationDetails: any = null;
  
  // Initialiser la subscription à null pour éviter l'erreur
  private consultationSubscription: Subscription | null = null;

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private sharedService: SharedService
  ) {}

  ngOnInit() {
    // S'abonner aux détails de la consultation
    this.consultationSubscription = this.sharedService.consultationDetails$.subscribe(details => {
      this.consultationDetails = details;
      if (this.consultationDetails && this.consultationDetails.id) {
        this.fetchBilanBiologique(this.consultationDetails.id); // Récupérer le bilan biologique
      }
    });
  }
  fetchBilanBiologique(consultationId: number): void {
    console.log('Consultation ID:', consultationId);
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + this.authService.getToken(),
    });
  
    this.http.get(`http://localhost:8000/bilan-bio/details-bilan/${consultationId}/`, { headers }).subscribe({
      next: (response: any) => {
        if (response ) {
          this.bioResults = response.map((param: any) => ({
            test: param.parameter || 'Inconnu',
            value: param.valeur || 'Non disponible',
            unit: param.unite || 'Non spécifié',
            reference: param.valeur_reference || 'Non défini'
          }));
        } else {
          console.error('Données invalides ou bilan manquant pour cette consultation');
          // Afficher un message plus explicite à l'utilisateur, si nécessaire
        }
      },
      error: (error) => {
        console.error('Erreur lors de la récupération du bilan biologique :', error);
        // Gestion de l'erreur, par exemple afficher un message à l'utilisateur
        alert('Erreur lors de la récupération du bilan biologique. Veuillez vérifier la consultation.');
      }
    });
  }

  ngOnDestroy() {
    // Désabonnement lorsque le composant est détruit pour éviter les fuites de mémoire
    if (this.consultationSubscription) {
      this.consultationSubscription.unsubscribe();
    }
  }

  openPopup() {
    this.isPopupOpen = true;
  }

  closePopup() {
    this.isPopupOpen = false;
  }

  addTest() {
    this.requestedTests.push('');
  }

  saveTests() {
    // Vérifier si consultationDetails est disponible
    if (!this.consultationDetails || !this.consultationDetails.id) {
      console.error('ID de consultation manquante');
      return;
    }

    if (this.requestedTests.length === 0) {
      console.error('Liste de tests vide');
      return;
    }

    const requestData = {
      tests: this.requestedTests,
      consultation_id: this.consultationDetails.id,
    };
     const headers = new HttpHeaders({
          'Authorization': 'Bearer ' + this.authService.getToken(),
        });
    // Appel à l'API pour enregistrer la demande de bilan biologique
    this.http.post('http://localhost:8000/bilan-bio/demande', requestData , { headers }).subscribe({
      next: (response: any) => {
        console.log('Réponse de l\'API :', response);
        this.isPopupOpen = false;
      },
      error: (error) => {
        console.error('Erreur lors de l\'enregistrement du bilan :', error);
      },
    });
  }
}

