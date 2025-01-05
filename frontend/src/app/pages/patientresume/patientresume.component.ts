import { Component } from '@angular/core';
import { ResumeComponent } from '../resume/resume.component';
import { OrdonanceComponent } from '../ordonance/ordonance.component';
import { BilanbioComponent } from '../bilanbio/bilanbio.component';
import { BilanradioComponent } from '../bilanradio/bilanradio.component';
import { CommonModule } from '@angular/common';
import { SharedService } from '../../services/sharedservice.service';



@Component({
  selector: 'app-patientresume',
  standalone: true,  
  templateUrl: './patientresume.component.html',
  styleUrls: ['./patientresume.component.css'],
  imports: [ ResumeComponent,OrdonanceComponent,BilanbioComponent,BilanradioComponent , CommonModule ] ,
})
export class PatientresumeComponent {
  currentSection: string = 'resume';
  title: string = '';
  date: string = '';
 consultationDetails : any;

  // Méthode pour changer la section active
  changeSection(section: string) {
    this.currentSection = section;
  }

  constructor( private sharedService : SharedService) { }
  
    ngOnInit(): void {
      // Récupérer les détails de la consultation depuis SharedService
      this.sharedService.consultationDetails$.subscribe((data) => {
        this.consultationDetails = data;
        console.log('Détails de la consultation dans ResumeComponent :', this.consultationDetails);
        this.title = data?.etablisement || ''; 
        this.date = data?.la_date || '';
      });
    }
  
}
