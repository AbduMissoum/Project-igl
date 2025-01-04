import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse,HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

import{SoinListForPatient,Soins,SoinsById,SoinsCreateRequestBody} from '../interfaces/soinsInterfaces';
import { AuthService } from './authservice.service';



@Injectable({
  providedIn: 'root'
})
export class SoinsService {
  private apiUrl = 'http://localhost:8000/'; // Adjust this to your API URL

  constructor(private http: HttpClient,private authService:AuthService) { }

  // Get all soins for a specific patient
  getSoinsByPatient(patientId: number): Observable<SoinListForPatient[]> {
      const headers = new HttpHeaders({
        'Authorization': 'Bearer ' + this.authService.getToken(), 
       })
    return this.http.get<SoinListForPatient[]>(`${this.apiUrl}/soins/patient/${patientId}/`,{headers})
      .pipe(
        catchError(this.handleError)
      );
  }

  // Get a specific soin by ID
  getSoinById(id: number): Observable<SoinsById> {
    return this.http.get<SoinsById>(`${this.apiUrl}/soins/${id}`)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Create a new soin
  createSoin(soin: Omit<SoinsCreateRequestBody, 'id'>): Observable<Soins> {
    return this.http.post<Soins>(`${this.apiUrl}/soins`, soin)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Update an existing soin
 
  // Delete a soin
  
  // Error handling
  private handleError(error: HttpErrorResponse) {
    let errorMessage = 'Une erreur est survenue';

    if (error.error instanceof ErrorEvent) {
      // Client-side error
      errorMessage = `Erreur: ${error.error.message}`;
    } else {
      // Server-side error
      errorMessage = `Code d'erreur: ${error.status}\nMessage: ${error.message}`;
    }

    console.error(errorMessage);
    return throwError(() => new Error(errorMessage));
  }

  // Helper method to format date for API
  formatDateForApi(date: Date): string {
    return date.toISOString();
  }

}