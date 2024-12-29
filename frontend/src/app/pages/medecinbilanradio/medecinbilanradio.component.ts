import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-medecinbilanradio',
  imports: [CommonModule , FormsModule],
  templateUrl: './medecinbilanradio.component.html',
  styleUrl: './medecinbilanradio.component.css'
})
export class MedecinbilanradioComponent {
  title = 'Bilan Radiologique';
  images = [
    { name: 'Radio du thorax', date: '2023-12-01' },
    { name: 'IRM cérébrale', date: '2023-11-20' }
  ];
  isPopupVisible: boolean = false;
  radioName: string = '';
  radiologistName: string = '';

  // Méthode pour afficher le pop-up
  openPopup(): void {
    this.isPopupVisible = true;
  }

  // Méthode pour fermer le pop-up
  closePopup(): void {
    this.isPopupVisible = false;
  }

  // Méthode pour soumettre la demande
  submitRequest(): void {
    console.log('Nom du Radio :', this.radioName);
    console.log('Nom du Radiologue :', this.radiologistName);

    // Ajouter la logique de soumission ici

    // Fermer le pop-up après soumission
    this.closePopup();
  }
}
