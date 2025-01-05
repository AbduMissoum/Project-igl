import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private baseUrl = "http://127.0.0.1:8000";
  private apiUrl = this.baseUrl+'/auth/login/';
  private logouturl= this.baseUrl+'/auth/logout/';
  private role: string | null = null;
  private patient_id: number | null = null;
  private token: string | null = null;

  constructor(private http: HttpClient) {}


  login(username: string, password: string): Observable<any> {
    // Retrieve the CSRF token from localStorage
   

    const body = { username, password };
  
    // Send the POST request to the backend with credentials included
    return this.http.post(this.baseUrl + '/api/token/', body, { withCredentials: true, });
  }  
  getInfo(username: string,password:string): Observable<any> {
    const body = { username, password };
   const headers = new HttpHeaders({
    'Authorization': 'Bearer ' + this.getToken(), 
   })
    return this.http.post(this.baseUrl+`/auth/login/`, body, { headers,withCredentials: true, });
  }

  logout(): Observable<any> {
    localStorage.removeItem('authToken');
    localStorage.removeItem('userRole');
    return this.http.post(this.logouturl, {withCredentials: true,});
  }

  setRole(role: string): void {
    this.role = role;
    localStorage.setItem('userRole', role); // Enregistre le rôle dans localStorage
  }
  setid(id: number): void {
    this.patient_id = id;
    localStorage.setItem('patient_id', id.toString());
  }
  clearid(): void {
    this.patient_id = null;
    localStorage.removeItem('patient_id'); // Supprime le rôle de localStorage
  }

  getid(): number | null {
    if (!this.patient_id) {
      const idString = localStorage.getItem('patient_id'); // Récupère l'ID stocké en tant que chaîne
      if (idString) {
        this.patient_id = parseInt(idString, 10); // Convertit la chaîne en un entier
      }
    }
    return this.patient_id || null; // Retourne l'ID converti ou null si non défini
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
  clearToken(): void {
    localStorage.removeItem('authToken'); // Sauvegarde le token dans localStorage
  }

  getToken(): string | null {
    return localStorage.getItem('authToken'); // Récupère le token depuis localStorage
  }

  // Méthode pour rechercher un patient par NSS
  getPatientByNSS(nss: string): Observable<any> {
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + this.getToken(), 
     })

    return this.http.get(this.baseUrl+`/patient?NSS=${nss}`, {headers, params: { NSS: nss } });
  }

  getPatientById(id: number): Observable<any> {
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + this.getToken(), 
     })
    return this.http.get<any>(this.baseUrl+`/patient/${id}`,{headers});
  }
}
