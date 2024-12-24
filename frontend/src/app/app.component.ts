import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { PatientresumeComponent } from './pages/patientresume/patientresume.component';

@Component({
  selector: 'app-root',
  imports: [ PatientresumeComponent ],
  templateUrl: './app.component.html',  
})
export class AppComponent {
  title = 'frontend';
}
