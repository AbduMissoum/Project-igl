import { Component } from '@angular/core';

import { FormsModule } from '@angular/forms';


import { AnalyseDemandeComponent } from "./pages/analyse-demande/analyse-demande.component";
import { RadioDemndesComponent } from "./pages/radio-demndes/radio-demndes.component";
import { SaisirAnalyseComponent } from "./pages/saisir-analyse/saisir-analyse.component";

@Component({
  selector: 'app-root',

  imports: [FormsModule,  SaisirAnalyseComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'

})
export class AppComponent {
  title = 'frontend';
}
