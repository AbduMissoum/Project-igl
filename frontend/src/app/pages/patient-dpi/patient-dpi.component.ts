import { Component } from '@angular/core';

@Component({
  selector: 'app-patient-dpi',
  standalone: true,  // Ce composant est Standalone
  imports: [],
  templateUrl: './patient-dpi.component.html',
  styleUrl: './patient-dpi.component.css'
})
export class PatientDPIComponent {
  constructor() { }

  ngOnInit(): void {
    console.log('Component initialized');}

}
