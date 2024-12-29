import { CommonModule } from '@angular/common';
import { Component , OnInit  } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { AuthService } from './services/authservice.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports :[RouterOutlet , RouterLink , CommonModule , FormsModule]
})
export class AppComponent implements OnInit {
  showHeader: boolean = false; // Header visible ou non
  userRole: string | null = null; // Rôle utilisateur

  constructor(private router: Router, private authService: AuthService) {
    // Écoute les changements de route
    this.router.events.subscribe(() => {
      this.showHeader = this.router.url !== '/login'; // Cache le header sur la page de login
      this.userRole = this.authService.getRole(); // Met à jour le rôle utilisateur
    });
  }

  ngOnInit(): void {
    this.userRole = this.authService.getRole(); // Synchronise le rôle au chargement initial
    console.log('showHeader:', this.showHeader);
    console.log('userRole:', this.userRole);
  }
  onLogout(): void {
    this.authService.logout().subscribe({
      next: (response) => {
        console.log(response.message); // Message de succès
        this.authService.clearRole(); // Supprime le rôle
        this.router.navigate(['/login']); // Redirige vers la page de login
      },
      error: (err) => {
        console.error('Erreur lors de la déconnexion:', err.error.message || err.message);
        alert('Erreur lors de la déconnexion.');
      },
    });
  }
  title = 'frontend';
}