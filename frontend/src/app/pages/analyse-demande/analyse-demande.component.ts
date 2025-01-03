import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from '../../services/authservice.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-analyse-demande',
  standalone: true,
  imports: [CommonModule  ],
  templateUrl: './analyse-demande.component.html',
  styleUrls: ['./analyse-demande.component.css']
})
export class AnalyseDemandeComponent implements OnInit {
  bilans: any[] = [];

  constructor(private http: HttpClient, private authService: AuthService , private router : Router) {}

  ngOnInit(): void {
    this.fetchBilans();
  }

  fetchBilans(): void {
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + this.authService.getToken(),
    });
    const url = 'http://localhost:8000/bilan-bio/notifications';
    this.http.get<any>(url, { headers }).subscribe({
      next: (response) => {
        console.log('Réponse brute de l\'API :', response);
        if (response ) {
          this.bilans = response; // Assurer que la réponse contient la clé message
        } else {
          alert('Aucune donnée trouvée. Vérifiez les filtres ou contactez l\'administrateur.');
        }
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des bilans :', err);
        alert('Erreur lors de la récupération des données. Veuillez réessayer plus tard.');
      }
    });
  }
  onRowClick(bilanId: string): void {
    this.router.navigate(['/saisiranalyse', bilanId]); // Navigation vers la page de détails
  }
}
