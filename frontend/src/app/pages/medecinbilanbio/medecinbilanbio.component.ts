import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-medecinbilanbio',
  imports: [CommonModule , FormsModule],
  templateUrl: './medecinbilanbio.component.html',
  styleUrl: './medecinbilanbio.component.css'
})
export class MedecinbilanbioComponent {
  title: string = 'Bilan Médical';
  isPopupOpen: boolean = false;
  requestedTests: string[] = []; // Liste des tests ajoutés
  nss: string = ''; // NSS du patient
  laborantin: string = ''; // Nom du laborantin

  bioResults = [
    { test: 'Glucose', value: '5.6', unit: 'mmol/L', reference: '3.9 - 6.1' },
    // Exemple de données
  ];

  // Ouvrir le popup
  openPopup() {
    this.isPopupOpen = true;
  }

  // Fermer le popup
  closePopup() {
    this.isPopupOpen = false;
  }

  // Ajouter une ligne pour un nouveau test
  addTest() {
    this.requestedTests.push('');
  }

  // Enregistrer les données et fermer le popup
  saveTests() {
    const requestData = {
      nss: this.nss,
      laborantin: this.laborantin,
      tests: this.requestedTests
    };
    console.log('Données enregistrées :', requestData);
    this.isPopupOpen = false;

    // Envoyez les données au backend ici via un service HTTP
  }

}
