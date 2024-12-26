import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-saisir-analyse',
  imports: [FormsModule , CommonModule],
  templateUrl: './saisir-analyse.component.html',
  styleUrl: './saisir-analyse.component.css'
})
export class SaisirAnalyseComponent {

   analyses = [
    { nom: 'Hémoglobine', resultat: '', unite: '', valRef: '' },
    { nom: 'Glucose', resultat: '', unite: '', valRef: '' },
    { nom: 'Cholestérol', resultat: '', unite: '', valRef: '' },
    { nom: 'Créatinine', resultat: '', unite: '', valRef: '' },
  ];

  onSubmit(): void {
    const incomplete = this.analyses.some(
      (analyse) =>
        !analyse.resultat || !analyse.unite || !analyse.valRef
    );

    if (incomplete) {
      alert('Veuillez remplir tous les champs.');
    } else {
      alert('Données envoyées avec succès !');
      console.log('Analyses:', this.analyses);
    }
  }

  onRetour(): void {
    alert('Retour à la page précédente.');
  }

}


