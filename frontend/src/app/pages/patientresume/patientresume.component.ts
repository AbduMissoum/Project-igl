import { Component } from '@angular/core';
import { ConsultationSectionComponent } from "../consultation-section/consultation-section.component";

@Component({
  selector: 'app-patientresume',
  standalone: true,  
  templateUrl: './patientresume.component.html',
  styleUrls: ['./patientresume.component.css'],
  imports: [ConsultationSectionComponent] ,
})
export class PatientresumeComponent {

  // Contenu dynamique
  currentSection = {
    title: 'LE RESUME DE LA CONSULTATION',
    content: 'Le contenu du résumé sera affiché ici.'
  };

  // Méthode pour changer la section
  changeSection(type: string) {
    if (type === 'resume') {
      this.currentSection = {
        title: 'LE RESUME DE LA CONSULTATION',
        content: 'Le contenu du résumé sera affiché ici.'
      };
    } else if (type === 'ordonnance') {
      this.currentSection = {
        title: "L'ORDONNANCE MÉDICALE",
        content: "Le contenu de l'ordonnance sera affiché ici."
      };
    } else if (type === 'biologique') {
      this.currentSection = {
        title: 'LE BILAN BIOLOGIQUE',
        content: 'Le contenu du bilan biologique sera affiché ici.'
      };
    } else if (type === 'radiologique') {
      this.currentSection = {
        title: 'LE BILAN RADIOLOGIQUE',
        content: 'Le contenu du bilan radiologique sera affiché ici.'
      };
    }
  }

  constructor() { }

  ngOnInit(): void {
    console.log('Component initialized');
    
  }
}
