import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { AuthService } from './services/authservice.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports :[RouterOutlet , RouterLink , CommonModule]
})
export class AppComponent {
  showHeader: boolean = true;
  userRole: string = '';
  constructor(private router: Router, private authService: AuthService) {
    // Vérifiez si le header doit être affiché
    this.router.events.subscribe(() => {
      this.showHeader = this.router.url !== '/login';
      this.userRole = this.authService.getRole(); // Récupérez le rôle utilisateur
    });
  }
  title = 'frontend';
}
