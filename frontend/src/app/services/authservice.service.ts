import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private baseUrl = "http://127.0.0.1:8000"
  private apiUrl = this.baseUrl+'/auth/login/';
  private logouturl= this.baseUrl+'/auth/logout/';
  private role: string | null = null;
  private csrftoken: string | null = null;

  constructor(private http: HttpClient) {}


  login(username: string, password: string): Observable<any> {
    // Retrieve the CSRF token from localStorage
   

    const body = { username, password };
  
    // Send the POST request to the backend with credentials included
    return this.http.post(this.apiUrl, body, { withCredentials: true, });
  }  

  logout(): Observable<any> {
    // Supprimer le token et le rôle à la déconnexion
    localStorage.removeItem('authToken');
    localStorage.removeItem('userRole');
    return this.http.post(this.logouturl, {withCredentials: true,});
  }

  setRole(role: string): void {
    this.role = role;
    localStorage.setItem('userRole', role); // Enregistre le rôle dans localStorage
  }
  setCsrfToken(csrftoken: string): void {
    this.csrftoken = csrftoken;
    localStorage.setItem('csrftoken', csrftoken); // Enregistre le rôle dans localStorage
  }

  getRole(): string | null {
    if (!this.role) {
      this.role = localStorage.getItem('userRole')!; // Récupère le rôle depuis localStorage si nécessaire
    }
    return this.role;
  }

  clearRole(): void {
    this.role = null;
    localStorage.removeItem('userRole'); // Supprime le rôle de localStorage
  }

  // Ajouter le token d'authentification
  setToken(token: string): void {
    localStorage.setItem('authToken', token); // Sauvegarde le token dans localStorage
  }

  getToken(): string | null {
    return localStorage.getItem('authToken'); // Récupère le token depuis localStorage
  }

  // Méthode pour rechercher un patient par NSS
  getPatientByNSS(nss: string): Observable<any> {
    return this.http.get(this.baseUrl+`/patient?NSS=${nss}`, { params: { NSS: nss } });
  }

  getPatientById(id: number): Observable<any> {
    return this.http.get<any>(this.baseUrl+`/patient/${id}`);
  }
}
