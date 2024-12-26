import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-saisir-soin',
  imports: [FormsModule , CommonModule ],
  templateUrl: './saisir-soin.component.html',
  styleUrl: './saisir-soin.component.css'
})
export class SaisirSoinComponent {
  onSubmit(formValues: any): void {

    const nss = (document.getElementById('nss') as HTMLInputElement).value;
    const date = (document.getElementById('date') as HTMLInputElement).value;
    const heure = (document.getElementById('heure') as HTMLInputElement).value;
    const soins = (document.getElementById('soins') as HTMLTextAreaElement).value;

    console.log({ nss, date, heure, soins });
  }

}



