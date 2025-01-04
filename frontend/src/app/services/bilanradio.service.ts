// bilan-radio.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './authservice.service';

@Injectable({
  providedIn: 'root',
})
export class BilanRadioService {
  private apiUrl = 'http://localhost:8000/bilan-radio/notifications'; // L'URL de l'API

  constructor(private http: HttpClient, private authService: AuthService) {}

  getBilanRadios(): Observable<any[]> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.authService.getToken()}`,
    });
    return this.http.get<any[]>(this.apiUrl, { headers });
  }
}
