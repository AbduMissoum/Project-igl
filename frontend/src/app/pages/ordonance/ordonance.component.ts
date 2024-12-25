import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-ordonance',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './ordonance.component.html',
  styleUrls: ['./ordonance.component.css']
})
export class OrdonanceComponent {
  title = 'Ordonnance';
  prescriptions = ['Médicament 1', 'Médicament 2', 'Médicament 3'];

}
