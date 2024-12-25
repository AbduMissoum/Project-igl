import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-medecinordonance',
  imports: [CommonModule],
  templateUrl: './medecinordonance.component.html',
  styleUrl: './medecinordonance.component.css'
})
export class MedecinordonanceComponent {
  title = 'Ordonnance';
  prescriptions = ['Médicament 1', 'Médicament 2', 'Médicament 3'];
}
