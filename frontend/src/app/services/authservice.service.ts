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
}
