import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { MedecinbilanbioComponent } from '../medecinbilanbio/medecinbilanbio.component';
import { MedecinbilanradioComponent } from '../medecinbilanradio/medecinbilanradio.component';
import { MedecinordonanceComponent } from '../medecinordonance/medecinordonance.component';
import { MedecinresumeComponent } from '../medecinresume/medecinresume.component';

@Component({
  selector: 'app-medecin',
  imports: [CommonModule , MedecinbilanbioComponent, MedecinbilanradioComponent, MedecinordonanceComponent, MedecinresumeComponent],
  templateUrl: './medecin.component.html',
  styleUrl: './medecin.component.css'
})
export class MedecinComponent {
  currentSection: string = 'resume';

  // Méthode pour changer la section active
  changeSection(section: string) {
    this.currentSection = section;
  }

  constructor() { }

  ngOnInit(): void {
    console.log('Component initialized');
    
  }

}
