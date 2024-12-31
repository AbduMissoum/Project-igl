import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ConsultationService {

  private apiUrl = '/consultations'; // Remplace par l'URL de ton API

  constructor(private http: HttpClient ) {}

  // Fonction pour envoyer une nouvelle consultation
 
  createConsultation(etablisement: string, dpi: number, laDate: string): Observable<any> {
const csrfToken = document.cookie.split("=")[1];    
    if (!csrfToken) {
      throw new Error('CSRF Token manquant');
    }
    
    // Ajouter le csrftoken dans les en-têtes de la requête
    const headers = new HttpHeaders({
      'X-CSRFToken': csrfToken // Ajouter le CSRF token dans l'en-tête
    });

    const body = {
      etablisement: etablisement,
      dpi: dpi,
      la_date: laDate,
    };
    return this.http.post('/api/consultations/', body, { headers ,withCredentials: true });
  }
  
 
}

