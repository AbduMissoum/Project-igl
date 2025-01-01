import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './authservice.service';

@Injectable({
  providedIn: 'root'
})
export class ConsultationService {
  private baseUrl = "http://127.0.0.1:8000/"
  private apiUrl = '/consultations'; // Remplace par l'URL de ton API

  constructor(private http: HttpClient ,private authService:AuthService) {}

  // Fonction pour envoyer une nouvelle consultation
 
  createConsultation(etablisement: string, dpi: number, laDate: string): Observable<any> {

    
    // Ajouter le csrftoken dans les en-têtes de la requête
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + this.authService.getToken(), 
     })

    const body = {
      etablisement: etablisement,
      dpi: dpi,
      la_date: laDate,
    };
    return this.http.post(this.baseUrl+'/consultations/', body, { headers ,withCredentials: true });
  }
  
 
}

