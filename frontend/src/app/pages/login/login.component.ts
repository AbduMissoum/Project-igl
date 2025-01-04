import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../services/authservice.service';
import { HttpClient,HttpHeaders } from '@angular/common/http';


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
       this.authService.setToken(response.access); // Appeler setToken pour sauvegarder le token
      this.authService.getInfo(this.username,this.password).subscribe({
        next:(response) => {
          const role = response.role;
          this.authService.setRole(role); // Appeler setRole pour sauvegarder le rôle
  
          // Redirection en fonction du rôle
          switch (role) {
            case 'admin':
              this.router.navigate(['/admin']);
              break;
            case 'patient':
              this.router.navigate(['/patient']);
              break;
            case 'medecin':
              this.router.navigate(['/rechercher']);
              break;
            case 'infirmier':
              this.router.navigate(['/saisirsoin']);
              break;
            case 'laborantin':
              this.router.navigate(['/analysedemande']);
              break;
            case 'radiologue':
              this.router.navigate(['/radiodemande']);
              break;
            default:
              console.error('Rôle utilisateur inconnu');
              break;
          }
        }
      })
    
    
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