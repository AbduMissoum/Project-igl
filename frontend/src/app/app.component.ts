import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SaisirSoinComponent } from './saisir-soin/saisir-soin.component';
import { FormsModule } from '@angular/forms';
import { RadioDemndesComponent } from './radio-demndes/radio-demndes.component';
import { Routes } from '@angular/router';
import { SaisirRadioComponent } from "./saisir-radio/saisir-radio.component";
import { AnalyseDemandeComponent } from "./analyse-demande/analyse-demande.component";
import { SaisirAnalyseComponent } from "./saisir-analyse/saisir-analyse.component";







import { PatientresumeComponent } from './pages/patientresume/patientresume.component';

@Component({
  selector: 'app-root',
<<<<<<< HEAD
  imports: [ PatientresumeComponent],
  templateUrl: './app.component.html',  
=======
  imports: [RouterOutlet, SaisirSoinComponent, FormsModule, RadioDemndesComponent, SaisirRadioComponent, AnalyseDemandeComponent, SaisirAnalyseComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
>>>>>>> origin/Mohamed
})
export class AppComponent {
  title = 'frontend';
}
