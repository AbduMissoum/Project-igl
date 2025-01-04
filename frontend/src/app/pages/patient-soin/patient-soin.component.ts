import { CommonModule ,} from '@angular/common';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { SharedService } from '../../services/sharedservice.service';
import { SoinsService } from '../../services/soinsService.sevice';
import { Subscription } from 'rxjs';
import { SoinListForPatient } from '../../interfaces/soinsInterfaces';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-patient-soin',
  imports :[FormsModule , CommonModule   ],
  templateUrl: './patient-soin.component.html',
  styleUrls: ['./patient-soin.component.css']
})
export class PatientSoinComponent implements OnInit, OnDestroy {
  soins: SoinListForPatient[] = [];
  hovered: number | null = null;
  private patientId: number = 0;
  private subscription: Subscription | null = null;

  constructor(
    private sharedService: SharedService,
    private soinsService: SoinsService
  ) {}

  ngOnInit(): void {
    this.subscription = this.sharedService.patientId$.subscribe({
      next: (id: number | null) => {
        if (id !== null) {
          this.patientId = id;
          this.loadSoins();
        }
      },
      error: (error) => {
        console.error('Erreur lors de la récupération de l\'ID du patient:', error);
      }
    });
  }

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  loadSoins(): void {
    this.soins = []; // Reset soins before loading new data
    this.soinsService.getSoinsByPatient(this.patientId).subscribe({
      next: (data:SoinListForPatient[]) => {
        this.soins = data.map((item: SoinListForPatient) => ({
          id: item.id,
          la_date: item.la_date,
          infirmier: item.infirmier,
          description: item.description,
          patient_id: item.patient_id,
        }));
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des soins:', err);
        // You might want to add error handling here, such as showing an error message to the user
      }
    });
  }
}