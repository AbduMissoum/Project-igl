import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PatientService {
  private apiUrl = 'http://localhost:8000/patient/'; // URL de l'API Django
  private patientData: any = null;
  constructor(private http: HttpClient) { }
  


  setPatientData(patient: any): void {
    this.patientData = patient;
  }

  getPatientData(): any {
    return this.patientData;
  }

  // Créer un patient
  createPatient(patientData: any): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json'
    });
    return this.http.post<any>('http://localhost:8000/patient/create/', patientData, { headers });
  }

  // Récupérer la liste des médecins traitants
  getMedecins(): Observable<any[]> {
    return this.http.get<any[]>('http://localhost:8000/patient/medecin/');
  }
}
