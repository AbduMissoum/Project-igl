import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-analyse-demande',
  imports: [CommonModule],
  templateUrl: './analyse-demande.component.html',
  styleUrl: './analyse-demande.component.css'
})
export class AnalyseDemandeComponent {
  analyses = [
    //A remplir shab l back
    { medecin: 'Dr. Dupont', patient: 'Jean Martin',  date: new Date('2024-12-20') },
    { medecin: 'Dr. Lefevre', patient: 'Marie Durand',  date: new Date('2024-12-22') },
    { medecin: 'Dr. Bernard', patient: 'Paul Leclerc',  date: new Date('2024-12-23') },
    { medecin: 'Dr. Martin', patient: 'Sophie Dubois',  date: new Date('2024-12-24') },
    { medecin: 'Dr. Lefevre', patient: 'Marie Durand',  date: new Date('2024-12-22') },
    { medecin: 'Dr. Bernard', patient: 'Paul Leclerc',  date: new Date('2024-12-23') },
    { medecin: 'Dr. Martin', patient: 'Sophie Dubois',  date: new Date('2024-12-24') }

  ];

  constructor(private router: Router) {}

  redirectToDetails(id: number): void {
    this.router.navigate(['/detailed-view', id]);
  }
  ngOnInit(): void {
  }


}








