import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from '../../services/authservice.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import Swal from 'sweetalert2'; // Import de SweetAlert2
import Chart from 'chart.js/auto';

interface Analyse {
  parametre: string;
  resultat: number;
  unite: string;
  valRef: string;
}

@Component({
  imports: [FormsModule, CommonModule],
  selector: 'app-saisir-analyse',
  templateUrl: './saisir-analyse.component.html',
  styleUrls: ['./saisir-analyse.component.css'],
})
export class SaisirAnalyseComponent implements OnInit {
  analyses: Analyse[] = [];
  bilanId: string = ''; // Pour stocker l'ID du bilan
  chart: any;
  chartRendered: boolean = false; // Indique si le graphe est affiché

  constructor(
    private activatedRoute: ActivatedRoute,
    private http: HttpClient,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.activatedRoute.params.subscribe((params) => {
      this.bilanId = params['id'];
      this.fetchBilan(this.bilanId);
    });
  }

  fetchBilan(bilanId: string): void {
    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.authService.getToken(),
    });
    const url = `http://localhost:8000/bilan-bio/voir-bilan/${bilanId}`;
    this.http.get<Analyse[]>(url, { headers }).subscribe({
      next: (response) => {
        if (response && response.length > 0) {
          this.analyses = response;
        } else {
          Swal.fire({
            icon: 'error',
            title: 'Erreur',
            text: 'Aucune donnée trouvée pour ce bilan.',
          });
        }
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des données du bilan :', err);
        Swal.fire({
          icon: 'error',
          title: 'Erreur',
          text: 'Erreur lors de la récupération des données.',
        });
      },
    });
  }

  generateGraph(): void {
    this.chartRendered = true; // Activer l'affichage du canvas

    setTimeout(() => {
      const canvas = document.getElementById('myBarChart') as HTMLCanvasElement;
      if (!canvas) {
        console.error('Le canevas pour le graphique n\'est pas disponible.');
        return;
      }

      const ctx = canvas.getContext('2d');
      if (!ctx) {
        console.error('Impossible d\'acquérir le contexte 2D du canevas.');
        return;
      }

      const labels = this.analyses.map((analyse) => analyse.parametre);
      const data = this.analyses.map((analyse) => analyse.resultat);
      const referenceData = this.analyses.map((analyse) => parseFloat(analyse.valRef) || 0);

      if (this.chart) {
        this.chart.destroy();
      }

      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels,
          datasets: [
            {
              label: 'Résultats des analyses',
              data,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1,
            },
            {
              label: 'Valeurs de référence',
              data: referenceData,
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              borderSkipped: 'bottom',
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    }, 0);
  }

  onSubmit(): void {
    const incomplete = this.analyses.some(
      (analyse) => !analyse.resultat || !analyse.unite || !analyse.valRef
    );

    if (incomplete) {
      Swal.fire({
        icon: 'warning',
        title: 'Attention',
        text: 'Veuillez remplir tous les champs.',
        customClass: {
          popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Utilise les classes valides de SweetAlert2
          title: 'text-2xl font-bold text-fonce', // Style du titre
          confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Bouton de confirmation
          cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]',
        },
      });
    } else {
      Swal.fire({
        title: 'Êtes-vous sûr ?',
        text: 'Voulez-vous vraiment envoyer ces données ?',
        icon: 'warning',
        showCancelButton: true,
       
        
        confirmButtonText: 'Oui, envoyer !',
        customClass: {
          popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Utilise les classes valides de SweetAlert2
          title: 'text-2xl font-bold text-fonce', // Style du titre
          confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Bouton de confirmation
          cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]',
        },
      }).then((result) => {
        if (result.isConfirmed) {
          this.updateBilan(this.bilanId); // Envoyer les données après confirmation
        }
      });
    }
  }

  updateBilan(bilanId: string): void {
    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.authService.getToken(),
      'Content-Type': 'application/json',
    });
    const url = `http://localhost:8000/bilan-bio/remplir/${bilanId}/`;

    const body = {
      param_valeurs: this.analyses.map((analyse) => ({
        parametre: analyse.parametre,
        valeur: analyse.resultat,
        unite: analyse.unite,
        valeur_reference: analyse.valRef,
      })),
    };

    this.http.put(url, body, { headers }).subscribe({
      next: (response: any) => {
        Swal.fire({
          icon: 'success',
          title: 'Succès',
          text: 'Bilan mis à jour avec succès !',
          customClass: {
            popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Utilise les classes valides de SweetAlert2
            title: 'text-2xl font-bold text-fonce', // Style du titre
            confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Bouton de confirmation
            cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]',
          },
        });
      },
      error: (err) => {
        console.error('Erreur lors de la mise à jour du bilan :', err);
        Swal.fire({
          icon: 'error',
          title: 'Erreur',
          text: 'Échec de la mise à jour.',
          customClass: {
            popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Utilise les classes valides de SweetAlert2
            title: 'text-2xl font-bold text-fonce', // Style du titre
            confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Bouton de confirmation
            cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]',
          },
        });
      },
    });
  }

  onRetour(): void {
    Swal.fire({
      title: 'Retour à la page précédente',
      text: 'Êtes-vous sûr ?',
      icon: 'question',
      showCancelButton: true,
     
      confirmButtonText: 'Oui, revenir !',
      customClass: {
        popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Utilise les classes valides de SweetAlert2
        title: 'text-2xl font-bold text-fonce', // Style du titre
        confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Bouton de confirmation
        cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]',
      },
    }).then((result) => {
      if (result.isConfirmed) {
        window.history.back();
      }
    });
  }
}
