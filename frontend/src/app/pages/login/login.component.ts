import { Component, Inject, OnInit } from '@angular/core';
import { PatientService } from '../../services/patient.service';
import { Ipatient } from '../../model/interface/patient';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [RouterLink],
  standalone: true,
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
connecter() {

}
  patient = Inject(PatientService);
  patientRole : String = '';
  constructor(){}
  ngOnInit(): void {
    this.patient.getPatient().subscribe((res : Ipatient)=>{
    this.patientRole = res.Nom;
    })
  
    
  }

}
