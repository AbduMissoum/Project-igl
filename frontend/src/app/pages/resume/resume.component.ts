import { Component } from '@angular/core';

@Component({
  selector: 'app-resume',
  standalone: true,
  templateUrl: './resume.component.html',
  styleUrls: ['./resume.component.css']
})
export class ResumeComponent {
  title = 'Résumé du patient';
  content = 'Ceci est un résumé des informations importantes du patient.';
}
