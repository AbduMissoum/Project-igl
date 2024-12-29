import { Component , ViewChild , ElementRef } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-saisir-radio',
  imports: [FormsModule , CommonModule ],
  templateUrl: './saisir-radio.component.html',
  styleUrl: './saisir-radio.component.css'
})
export class SaisirRadioComponent {
  // Tableau initial vide
  rows: Array<{ analysis: string; result: string; unit: string; reference: string }> = [];

  // Indique si le graphe est généré
  graphGenerated = false;
  generatedGraph: string = '';

 
 

  // Générer un graphe
  generateGraph() {
    // Vérifier que des données existent
    if (this.rows.length === 0) {
      alert('Veuillez ajouter des données avant de générer le graphe.');
      return;
    }

    // Simulation de génération de graphe (à remplacer par votre propre logique)
    this.graphGenerated = true;
    this.generatedGraph = 'assets/images/generated-graph.png'; // Chemin de l'image générée
  }
}





