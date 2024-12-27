import { Component } from '@angular/core';
import { ResumeComponent } from '../resume/resume.component';
import { OrdonanceComponent } from '../ordonance/ordonance.component';
import { BilanbioComponent } from '../bilanbio/bilanbio.component';
import { BilanradioComponent } from '../bilanradio/bilanradio.component';
import { CommonModule } from '@angular/common';



@Component({
  selector: 'app-patientresume',
  standalone: true,  
  templateUrl: './patientresume.component.html',
  styleUrls: ['./patientresume.component.css'],
  imports: [ ResumeComponent,OrdonanceComponent,BilanbioComponent,BilanradioComponent , CommonModule ] ,
})
export class PatientresumeComponent {

  
 
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
