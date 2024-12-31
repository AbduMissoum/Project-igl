import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private patientIdSource = new BehaviorSubject<number | null>(null);
  patientId$ = this.patientIdSource.asObservable();

  updatePatientId(id: number): void {
    this.patientIdSource.next(id);
  }
}
