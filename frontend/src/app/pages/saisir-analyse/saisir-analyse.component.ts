import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from '../../services/authservice.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

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
  styleUrls: ['./saisir-analyse.component.css']
})
export class SaisirAnalyseComponent implements OnInit {
  analyses: Analyse[] = [];
  bilanId: string = ''; // Pour stocker l'ID du bilan

  constructor(
    private activatedRoute: ActivatedRoute, // Pour accéder aux paramètres de l'URL
    private http: HttpClient,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    // Récupérer l'ID du bilan depuis l'URL
    this.activatedRoute.params.subscribe(params => {
      this.bilanId = params['id']; // Récupère le bilan_id de l'URL
      this.fetchBilan(this.bilanId); // Appeler la méthode pour récupérer les données du bilan
    });
  }

  // Récupérer les données du bilan avec l'ID
  fetchBilan(bilanId: string): void {
    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.authService.getToken()
    });
    const url = `http://localhost:8000/bilan-bio/voir-bilan/${bilanId}`;
    this.http.get<Analyse[]>(url, { headers }).subscribe({
      next: (response) => {
        console.log('Réponse brute de l\'API :', response);
        if (response && response.length > 0) {
          this.analyses = response; // Mettez à jour le tableau d'analyses avec les données reçues
        } else {
          alert('Aucune donnée trouvée pour ce bilan.');
        }
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des données du bilan :', err);
        alert('Erreur lors de la récupération des données. Veuillez réessayer plus tard.');
      }
    });
  }

  // Méthode pour envoyer les données au backend via une requête PUT
  updateBilan(bilanId: string): void {
    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.authService.getToken(),
      'Content-Type': 'application/json'
    });
    const url = `http://localhost:8000/bilan-bio/remplir/${bilanId}/`;

    // Construire le corps de la requête
    const body = {
      param_valeurs: this.analyses.map(analyse => ({
        parametre: analyse.parametre,
        valeur: analyse.resultat,
        unite: analyse.unite,
        valeur_reference: analyse.valRef
      }))
    };
    console.log("jfedef" ,body);


    this.http.put(url, body,  { headers }).subscribe({
      next: (response: any) => {
        alert('Bilan mis à jour avec succès !');
        console.log('Réponse du serveur :', response);
      },
      error: (err) => {
        console.error('Erreur lors de la mise à jour du bilan :', err);
        alert('Échec de la mise à jour. Veuillez vérifier les données et réessayer.');
      }
    });
  }

  onSubmit(): void {
    const incomplete = this.analyses.some(
      (analyse) =>
        !analyse.resultat || !analyse.unite || !analyse.valRef
    );

    if (incomplete) {
      alert('Veuillez remplir tous les champs.');
    } else {
      this.updateBilan(this.bilanId); // Appeler la méthode pour mettre à jour le bilan
    }
  }

  onRetour(): void {
    alert('Retour à la page précédente.');
  }
}
