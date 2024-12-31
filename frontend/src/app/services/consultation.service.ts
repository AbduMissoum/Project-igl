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
    const csrfToken = this.getCSRFTokenFromCookies();

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
    return this.http.post('http://localhost:8000/consultations/', body);
  }
  private getCSRFTokenFromCookies(): string {
    const name = 'csrftoken=';
    const cookies = document.cookie.split(';');
    console.log(cookies);
    for (let i = 0; i < cookies.length; i++) {
      let c = cookies[i].trim();
      if (c.indexOf(name) === 0) {
        return c.substring(name.length, c.length);
      }
    }
    return ''; // Retourner une chaîne vide si le token CSRF n'est pas trouvé
  }
}

