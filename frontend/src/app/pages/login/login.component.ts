import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../services/authservice.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  imports :[FormsModule , CommonModule   ],
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username: string = ''; // Champs liés au formulaire
  password: string = '';

  constructor(private router: Router, private authService: AuthService) {}

  ngOnInit(): void {}

  onLogin(): void {
    if (!this.username || !this.password) {
      console.error('Le nom d’utilisateur et le mot de passe sont requis.');
      return;
    }

    this.authService.login(this.username, this.password).subscribe({
      next: (response) => {
        console.log('Connexion réussie:', response);

        // Définir le rôle utilisateur
        const role = response.role;
        this.authService.setRole(role); // Appeler setRole pour sauvegarder le rôle

        // Redirection en fonction du rôle
        switch (role) {
          case 'admin':
            this.router.navigate(['/admin']);
            break;
          case 'Patient':
            this.router.navigate(['/patient']);
            break;
          case 'medecin':
            this.router.navigate(['/medecin']);
            break;
          case 'Infirmier':
            this.router.navigate(['/saisirsoin']);
            break;
          case 'Laborantin':
            this.router.navigate(['/saisiranalyse']);
            break;
          case 'Radiologue':
            this.router.navigate(['/saisirradio']);
            break;
          default:
            console.error('Rôle utilisateur inconnu');
            break;
        }
      },
      error: (err) => {
        if (err.status === 400 || err.status === 404) {
          console.error('Erreur de connexion:', err.error.message);
          alert(err.error.message);
        } else {
          console.error('Erreur inconnue:', err);
        }
      },
    });
  }
}