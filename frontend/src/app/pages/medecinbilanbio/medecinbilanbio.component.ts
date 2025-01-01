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
  requestedTests: string[] = []; 
  nss: string = '';
  laborantin: string = ''; 

  bioResults = [
    { test: 'Glucose', value: '5.6', unit: 'mmol/L', reference: '3.9 - 6.1' },
   
  ];

  
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
    const requestData = {
      nss: this.nss,
      laborantin: this.laborantin,
      tests: this.requestedTests
    };
    console.log('Données enregistrées :', requestData);
    this.isPopupOpen = false;
  }

}
