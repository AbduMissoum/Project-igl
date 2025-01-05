import { CommonModule } from '@angular/common';
import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SoinsService } from '../../services/soinsService.sevice';
import { SoinListForPatient } from '../../interfaces/soinsInterfaces';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-soins',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './soins.component.html',
  styleUrls: ['./soins.component.css'] // Corrected property name
})
export class SoinsComponent implements OnInit, OnDestroy {
  soins: SoinListForPatient[] = [];
  hovered: SoinListForPatient | null = null;

  private patientId: number | null = null;
  private subscription: Subscription | null = null;

  constructor(private soinsService: SoinsService) {}

  ngOnInit(): void {
    // Récupérer l'ID du patient depuis localStorage
    const patientIdString = localStorage.getItem('patient_id');
    if (patientIdString) {
      const patientId = parseInt(patientIdString, 10);
      if (!isNaN(patientId)) {
        this.patientId = patientId;
        this.loadSoins();
      } else {
        console.error("L'ID du patient n'est pas valide.");
      }
    } else {
      console.error('Aucun ID patient trouvé dans localStorage.');
    }
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe();
  }

  loadSoins(): void {
    if (!this.patientId) {
      console.warn('ID patient manquant, impossible de charger les soins.');
      return;
    }

    this.soinsService.getSoinsByPatient(this.patientId).subscribe({
      next: (data: SoinListForPatient[]) => {
        this.soins = data.map((item: SoinListForPatient) => ({
          id: item.id,
          la_date: item.la_date,
          infirmier: item.infirmier,
          description: item.description,
          patient_id: item.patient_id,
        }));
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des soins :', err);
      }
    });
  }
}
