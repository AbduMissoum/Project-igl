import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-patient-soin',
  templateUrl: './patient-soin.component.html',
  imports :[CommonModule],
  styleUrl: './patient-soin.component.css'
})
export class PatientSoinComponent {
  soins = [
    {
      infirmier: 'Jean Dupont',
      etablissement: 'Clinique Sainte-Marie',
      date: '2024-12-27',
      heure: '10:30',
      details: 'Injection d\'antibiotiques pour traiter une infection respiratoire.',
    },
    {
      infirmier: 'Sophie Martin',
      etablissement: 'Hôpital Général',
      date: '2024-12-26',
      heure: '14:00',
      details: 'Pansement appliqué sur une plaie chirurgicale suite à une opération.',
    },
    {
      infirmier: 'Paul Leroy',
      etablissement: 'Centre Médical',
      date: '2024-12-25',
      heure: '09:00',
      details: 'Suivi post-opératoire et vérification des signes vitaux du patient.',
    },
  ];

  hovered: any = null; // Stocke le soin survolé
  constructor() { }

  ngOnInit(): void {
    console.log('Component initialized');}

}
