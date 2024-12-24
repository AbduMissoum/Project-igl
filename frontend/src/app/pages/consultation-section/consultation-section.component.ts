import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-consultation-section',
  standalone: true, 
  templateUrl: './consultation-section.component.html',
  styleUrls: ['./consultation-section.component.css']
})
export class ConsultationSectionComponent {
  @Input() title: string = ''; // Titre de la section
  @Input() content: string = ''; // Contenu de la section
}
