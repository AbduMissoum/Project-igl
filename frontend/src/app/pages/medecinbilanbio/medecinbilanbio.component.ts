import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { Chart } from 'chart.js';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { SharedService } from '../../services/sharedservice.service';
import { Subscription } from 'rxjs';
import { AuthService } from '../../services/authservice.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-medecinbilanbio',
  imports: [CommonModule, FormsModule],
  templateUrl: './medecinbilanbio.component.html',
  styleUrls: ['./medecinbilanbio.component.css'],
})
export class MedecinbilanbioComponent implements OnInit {

  // Variables pour gérer le graphique
  @ViewChild('myBarChart') myBarChart: ElementRef | undefined;
  chartRendered: boolean = false;
  chart: any;

  // Autres variables
  title: string = 'Bilan Médical';
  isPopupOpen: boolean = false;
  requestedTests: { name: string }[] = [{ name: 'Nom du test' }];

  nss: string = '';
  laborantin: string = '';
  bioResults = [
    { test: 'No test', value: 0, unit: 'No Unité', reference: 'No reference' },
  ];

  consultationDetails: any = null;
  private consultationSubscription: Subscription | null = null;

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private sharedService: SharedService
  ) {}

  ngOnInit() {
    this.consultationSubscription = this.sharedService.consultationDetails$.subscribe((details) => {
      this.consultationDetails = details;
      if (this.consultationDetails && this.consultationDetails.id) {
        this.fetchBilanBiologique(this.consultationDetails.id);
      } else {
        console.error('Consultation details are missing or invalid');
      }
    });
  }

  supprimer() {
    if (this.requestedTests.length > 1) {
      this.requestedTests.pop(); // Supprime le dernier élément du tableau
    } else {
      Swal.fire({
        title: 'Attention',
        text: 'Il doit y avoir au moins un test dans la liste.',
        icon: 'warning',
        confirmButtonText: 'OK',
        customClass: {
          popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center',
          title: 'text-2xl font-bold text-fonce',
          confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]',
        },
      });
    }
  }

  // Fetch des résultats de bilan biologique
  fetchBilanBiologique(consultationId: number): void {
    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.authService.getToken(),
    });

    this.http
      .get(`http://localhost:8000/bilan-bio/details-bilan/${consultationId}/`, { headers })
      .subscribe({
        next: (response: any) => {
          this.bioResults = response.map((param: any) => ({
            test: param.parametre || 'Inconnu',
            value: param.valeur || 'Non disponible',
            unit: param.unite || 'Non spécifié',
            reference: param.valeur_reference || 'Non défini',
          }));
        },
        error: (error) => {
          console.error('Erreur lors de la récupération du bilan biologique :', error);
          Swal.fire({
            title: 'Erreur',
            text: 'Impossible de récupérer les détails du bilan biologique.',
            icon: 'error',
            confirmButtonText: 'OK',
            customClass: {
              popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center',
              title: 'text-2xl font-bold text-fonce',
              confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]',
            },
          });
        },
      });
  }

  generateGraph() {
    const labels = this.bioResults.map((result) => result.test);
    const data = this.bioResults.map((result) => result.value);

    // Convertir les valeurs de référence en nombres
    const referenceData = this.bioResults.map((result) => {
      const referenceValue = parseFloat(result.reference);
      return isNaN(referenceValue) ? 0 : referenceValue; // Si la valeur n'est pas un nombre, on la remplace par 0
    });

    if (this.chart) {
      this.chart.destroy(); // Détruit l'ancien graphique si existe
    }

    this.chart = new Chart(this.myBarChart?.nativeElement, {
      type: 'bar', // Type de graphique : barres
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Résultats des tests biologiques',
            data: data,
            backgroundColor: 'rgba(93, 165, 185, 0.5)', // Couleur pour les résultats
            borderColor: 'rgba(93, 165, 185, 1)',
            borderWidth: 1,
          },
          {
            label: 'Valeur de référence',
            data: referenceData,
            backgroundColor: 'rgba(255, 99, 132, 0.5)', // Couleur pour les valeurs de référence
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });

    this.chartRendered = true;
  }

  openPopup() {
    this.isPopupOpen = true;
  }

  closePopup() {
    this.isPopupOpen = false;
  }

  addTest() {
    this.requestedTests.push({ name: '' });
  }

  removeTest(index: number) {
    this.requestedTests.splice(index, 1);
  }

  saveTests() {
    const tests = this.requestedTests.map((test) => test.name.trim()).filter((name) => name !== '');

    if (tests.length === 0) {
      Swal.fire({
        title: 'Attention',
        text: 'Ajoutez au moins un test.',
        icon: 'warning',
        confirmButtonText: 'OK',
        customClass: {
          popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center',
          title: 'text-2xl font-bold text-fonce',
          confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]',
        },
      });
      return;
    }

    const requestData = {
      tests,
      consultation_id: this.consultationDetails?.id || 0,
      nss: this.nss,
      laborantin: this.laborantin,
    };

    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.authService.getToken(),
    });

    this.http.post('http://localhost:8000/bilan-bio/demande', requestData, { headers }).subscribe({
      next: (response) => {
        Swal.fire({
          title: 'Succès',
          text: 'Demande de bilan enregistrée avec succès.',
          icon: 'success',
          confirmButtonText: 'OK',
          customClass: {
            popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center',
            title: 'text-2xl font-bold text-fonce',
            confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]',
          },
        });
        this.isPopupOpen = false;
        this.requestedTests = [];
        this.nss = '';
        this.laborantin = '';
      },
      error: (error) => {
        console.error('Erreur lors de l\'enregistrement du bilan :', error);
        Swal.fire({
          title: 'Erreur',
          text: 'Erreur lors de l\'enregistrement de la demande de bilan.',
          icon: 'error',
          confirmButtonText: 'OK',
          customClass: {
            popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center',
            title: 'text-2xl font-bold text-fonce',
            confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]',
          },
        });
      },
    });
  }

  ngOnDestroy() {
    if (this.consultationSubscription) {
      this.consultationSubscription.unsubscribe();
    }
  }
}
