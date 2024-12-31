import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private apiUrl = 'http://127.0.0.1:8000/auth/login/';
  private role: string | null = null;

  constructor(private http: HttpClient) {}

  login(username: string, password: string): Observable<any> {
    const body = { username, password };
    return this.http.post(this.apiUrl, body);
  }

  logout(): Observable<any> {
    // Supprimer le token et le rôle à la déconnexion
    localStorage.removeItem('authToken');
    localStorage.removeItem('userRole');
    return this.http.post('http://127.0.0.1:8000/auth/logout/', {});
  }

  setRole(role: string): void {
    this.role = role;
    localStorage.setItem('userRole', role); // Enregistre le rôle dans localStorage
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
    return this.http.get(`http://127.0.0.1:8000/patient?NSS=${nss}`, { params: { NSS: nss } });
  }

  getPatientById(id: number): Observable<any> {
    return this.http.get<any>(`http://127.0.0.1:8000/patient/${id}`);
  }
}
