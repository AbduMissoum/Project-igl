import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { QRCodeComponent } from 'angularx-qrcode';

@Component({
  selector: 'app-patient-dpi',
  standalone: true,  // Ce composant est Standalone
  imports: [ CommonModule , QRCodeComponent  ],
  templateUrl: './patient-dpi.component.html',
  styleUrl: './patient-dpi.component.css'
})
export class PatientDPIComponent {

  nss: string = '123456789012345'; // Exemple de NSS
  qrCodeData: string = ''; // Stockage du QR Code

  ngOnInit(): void {
   
  }

  

  constructor() { }

  

}
