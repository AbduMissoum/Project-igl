import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MedecinbilanbioComponent } from '../medecinbilanbio/medecinbilanbio.component';
import { MedecinbilanradioComponent } from '../medecinbilanradio/medecinbilanradio.component';
import { MedecinordonanceComponent } from '../medecinordonance/medecinordonance.component';
import { MedecinresumeComponent } from '../medecinresume/medecinresume.component';
import { SharedService } from '../../services/sharedservice.service';

@Component({
  selector: 'app-medecin',
  imports: [CommonModule , MedecinbilanbioComponent, MedecinbilanradioComponent, MedecinordonanceComponent, MedecinresumeComponent],
  templateUrl: './medecin.component.html',
  styleUrl: './medecin.component.css'
})
export class MedecinComponent implements OnInit {
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
