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

  openPopup() {
    this.isPopupOpen = true;
  }

  closePopup() {
    this.isPopupOpen = false;
  }

  addTest() {
    this.requestedTests.push('');
  }

  removeTest(index: number) {
    this.requestedTests.splice(index, 1);
  }

  saveTests() {
    if (!this.nss || !this.laborantin) {
      alert('Veuillez remplir les champs NSS et Laborantin.');
      return;
    }

    if (this.requestedTests.length === 0) {
      alert('Ajoutez au moins un test.');
      return;
    }

    const requestData = {
      tests: this.requestedTests.filter((test) => test.trim() !== ''), // Supprime les champs vides
      consultation_id: this.consultationDetails?.id || 0,
      nss: this.nss,
      laborantin: this.laborantin,
    };

    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.authService.getToken(),
    });

    this.http.post('http://localhost:8000/bilan-bio/demande', requestData, { headers }).subscribe({
      next: (response) => {
        alert('Demande de bilan enregistrée avec succès.');
        this.isPopupOpen = false;
        this.requestedTests = [];
        this.nss = '';
        this.laborantin = '';
      },
      error: (error) => {
        console.error('Erreur lors de l\'enregistrement du bilan :', error);
        alert('Erreur lors de l\'enregistrement de la demande de bilan.');
      },
    });
  }

  ngOnDestroy() {
    if (this.consultationSubscription) {
      this.consultationSubscription.unsubscribe();
    }
  }
}
