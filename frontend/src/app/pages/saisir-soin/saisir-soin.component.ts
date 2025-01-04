import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SoinsService } from '../../services/soinsService.sevice';
@Component({
  selector: 'app-saisir-soin',
  imports: [FormsModule , CommonModule ],
  templateUrl: './saisir-soin.component.html',
  styleUrl: './saisir-soin.component.css'
})
export class SaisirSoinComponent {
  constructor(private soinsService : SoinsService) { }
  onSubmit(): void {
console.log("hhhhhhh")
    const nss = (document.getElementById('nss') as HTMLInputElement).value;
    const date = (document.getElementById('date') as HTMLInputElement).value;
    const soins = (document.getElementById('soins') as HTMLTextAreaElement).value;
   const body = {NSS : nss, la_date: date, description : soins};
   
   this.soinsService.createSoin(body).subscribe({next : (data) => {
      console.log('Soin créé avec succès:', data);
    },
    error: (err) => {
      console.error('Erreur lors de la création du soin:', err);
    }
  });
  }

}



