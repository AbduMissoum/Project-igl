import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';



@Component({
  selector: 'app-radio-demndes',
  imports: [CommonModule ],
  templateUrl: './radio-demndes.component.html',
  styleUrl: './radio-demndes.component.css'
})
export class RadioDemndesComponent {
  radios = [
    //A remplir shab l back
    { medecin: 'Dr. Dupont', patient: 'Jean Martin', type: 'Radiographie thoracique', date: new Date('2024-12-20') },
    { medecin: 'Dr. Lefevre', patient: 'Marie Durand', type: 'Scanner abdominal', date: new Date('2024-12-22') },
    { medecin: 'Dr. Bernard', patient: 'Paul Leclerc', type: 'IRM cérébrale', date: new Date('2024-12-23') },
    { medecin: 'Dr. Martin', patient: 'Sophie Dubois', type: 'Radiographie dentaire', date: new Date('2024-12-24') },
    { medecin: 'Dr. Lefevre', patient: 'Marie Durand', type: 'Scanner abdominal', date: new Date('2024-12-22') },
    { medecin: 'Dr. Bernard', patient: 'Paul Leclerc', type: 'IRM cérébrale', date: new Date('2024-12-23') },
    { medecin: 'Dr. Martin', patient: 'Sophie Dubois', type: 'Radiographie dentaire', date: new Date('2024-12-24') }

  ];

  constructor(private router: Router) {}

  redirectToDetails(id: number): void {
    this.router.navigate(['/detailed-view', id]);
  }
  ngOnInit(): void {
  }

}



