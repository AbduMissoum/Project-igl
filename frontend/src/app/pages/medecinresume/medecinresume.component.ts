import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-medecinresume',
  imports: [CommonModule],
  templateUrl: './medecinresume.component.html',
  styleUrl: './medecinresume.component.css'
})
export class MedecinresumeComponent {
  title = 'Résumé du patient';
  content = 'Ceci est un résumé des informations importantes du patient.';

}
