import { Component } from '@angular/core';

@Component({
  selector: 'app-admin-page',
  standalone: true,  // Ce composant est Standalone
  templateUrl: './admin-page.component.html',  // Fichier HTML de la page d'administration
  styleUrls: ['./admin-page.component.css'],  // Fichier CSS de la page d'administration
})
export class AdminPageComponent {
  constructor() { }

  ngOnInit(): void {
    console.log('AdminPageComponent initialized');
    // Logique de la page admin
  }
}
