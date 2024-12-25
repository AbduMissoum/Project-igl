import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';


// import { PatientresumeComponent } from "./pages/patientresume/patientresume.component";
import { ContactComponent } from './pages/contact/contact.component';

@Component({
  selector: 'app-root',
  imports: [  ContactComponent],
  templateUrl: './app.component.html',  
})
export class AppComponent {
  title = 'frontend';
}
