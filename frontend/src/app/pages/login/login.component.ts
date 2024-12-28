import { Component, Inject, OnInit } from '@angular/core';
import { PatientService } from '../../services/patient.service';
import { Ipatient } from '../../model/interface/patient';
import { Router, RouterLink } from '@angular/router';
import { routes } from '../../app.routes';
import { AuthService } from '../../services/authservice.service';

@Component({
  selector: 'app-login',
  imports: [RouterLink , ],
  standalone: true,
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
  userRole: string = ''; // Propriété de la classe

  constructor(private router: Router, private authService: AuthService) {}

  onLogin(): void {
    this.authService.setRole(this.userRole); // Utilisez la valeur définie dans `userRole`

    // Redirigez selon le rôle
    switch (this.userRole) {
      case 'admin':
        this.router.navigate(['/admin']);
        break;
      case 'Patient':
        this.router.navigate(['/patient']);
        break;
      case 'Medecin':
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
  }

  ngOnInit(): void {
    // Initialisation ou récupération depuis le backend
    this.userRole = 'Patient'; // Valeur par défaut pour les tests
  }
  

}
