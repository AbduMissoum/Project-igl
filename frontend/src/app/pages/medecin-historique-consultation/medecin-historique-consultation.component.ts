import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {  RouterLink } from '@angular/router';


interface Historique {
  medecin: string;
  etablissement: string;
  date: Date;
  heure: string;
}

@Component({
  selector: 'app-medecin-historique-consultation',
  standalone: true,
  imports: [CommonModule , FormsModule , RouterLink , ],
  templateUrl: './medecin-historique-consultation.component.html',
  styleUrls: ['./medecin-historique-consultation.component.css']
})
export class MedecinHistoriqueConsultationComponent {
  historiques: Historique[] = [
    { medecin: 'Dr. Dupont', etablissement: 'Clinique Saint-Martin', date: new Date('2024-12-20'), heure: '10:30' },
    { medecin: 'Dr. Lefevre', etablissement: 'Hôpital Central', date: new Date('2024-12-22'), heure: '14:00' },
    { medecin: 'Dr. Bernard', etablissement: 'Centre Médical Nord', date: new Date('2024-12-23'), heure: '09:15' },
    { medecin: 'Dr. Martin', etablissement: 'Polyclinique Sud', date: new Date('2024-12-24'), heure: '16:45' }
  ];

  // Variable pour gérer l'ouverture/fermeture du modal
  isModalOpen: boolean = false;

  // Modèle pour la nouvelle consultation
  newConsultation: Historique = { medecin: '', etablissement: '', date: new Date(), heure: '' };

  constructor() {}

  ngOnInit(): void {
    console.log('Component initialized');
  }

  openModal(): void {
    this.isModalOpen = true;
  }

  closeModal(): void {
    this.isModalOpen = false;
  }

  addConsultation(): void {
    if (this.newConsultation.medecin && this.newConsultation.etablissement && this.newConsultation.date && this.newConsultation.heure) {
      // Ajouter la nouvelle consultation à la liste
      this.historiques.push({
        ...this.newConsultation,
        date: new Date(this.newConsultation.date) // S'assurer que la date est correctement formatée
      });

      // Réinitialiser le formulaire
      this.newConsultation = { medecin: '', etablissement: '', date: new Date(), heure: '' };
      this.closeModal();
    }
  }
}