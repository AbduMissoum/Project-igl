import { Component, OnInit } from '@angular/core';
import { BilanRadioService } from '../../services/bilanradio.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-radio-demndes',
  imports: [CommonModule, FormsModule],
  templateUrl: './radio-demndes.component.html',
  styleUrls: ['./radio-demndes.component.css'],
})
export class RadioDemndesComponent implements OnInit {
  radios: any[] = []; // Tableau pour stocker les bilans radiologiques récupérés

  constructor(private bilanRadioService: BilanRadioService , private router : Router) {}

  ngOnInit(): void {
    // Récupérer les bilans radiologiques depuis l'API
    this.bilanRadioService.getBilanRadios().subscribe({
      next: (data) => {
        this.radios = data;
        console.log('Données des bilans récupérées :', this.radios); // Pour déboguer
      },
      error: (error) => {
        console.error('Erreur lors de la récupération des bilans radiologiques:', error);
      },
    });
  }

  onRowClick(radioid: string): void {
    this.router.navigate(['/saisirradio', radioid]); // Navigation vers la page de détails
  }
}
