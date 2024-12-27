import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';


interface Historique {
  medecin: string;
  etablissement: string;
  date: Date;
  heure: string;
}
@Component({
  selector: 'app-patient-consultation-historique',
  imports: [ CommonModule],
  templateUrl: './patient-consultation-historique.component.html',
  styleUrl: './patient-consultation-historique.component.css'
})
export class PatientConsultationHistoriqueComponent {

  historiques: Historique[] = [
    { medecin: 'Dr. Dupont', etablissement: 'Clinique Saint-Martin', date: new Date('2024-12-20'), heure: '10:30' },
    { medecin: 'Dr. Lefevre', etablissement: 'Hôpital Central', date: new Date('2024-12-22'), heure: '14:00' },
    { medecin: 'Dr. Bernard', etablissement: 'Centre Médical Nord', date: new Date('2024-12-23'), heure: '09:15' },
    { medecin: 'Dr. Martin', etablissement: 'Polyclinique Sud', date: new Date('2024-12-24'), heure: '16:45' }
  ];

  constructor() { }

  ngOnInit(): void {
    console.log('Component initialized');}

}
