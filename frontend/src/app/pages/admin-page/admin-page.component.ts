import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-admin-page',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.css'],
})
export class AdminPageComponent implements OnInit {
  // Variables pour gérer les médecins et leur filtrage
  medecins: any[] = [];
  filteredMedecins: any[] = [];
  selectedMedecinId: number | null = null;
  selectedMedecinName: string = '';
  isListVisible: boolean = false;

  patientData = {
    NSS: '',
    nom: '',
    prenom: '',
    date_naissance: '',
    adresse: '',
    tel: '',
    mutuelle: '',
    email: '',
    medecin_traitant: ''  // Nom du médecin sélectionné
  };

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadMedecins();
  }

  // Fonction pour charger les médecins depuis l'API
  loadMedecins() {
    this.http.get<any[]>('http://127.0.0.1:8000/patient/medecin/')
      .subscribe((response) => {
        this.medecins = response;
        this.filteredMedecins = response;
        // Initialement, afficher tous les médecins
      });
  }

  // Fonctions pour gérer l'affichage de la liste des médecins
  showList() {
    this.isListVisible = true;
  }

  hideList() {
    this.isListVisible = false;
  }

  // Fonction pour filtrer la liste des médecins selon l'input utilisateur
  filterMedecins(event: any) {
    const query = event.target.value.toLowerCase();
    this.filteredMedecins = this.medecins.filter((medecin) =>
      medecin.username.toLowerCase().includes(query)
    );
  }

  // Fonction pour sélectionner un médecin
  selectMedecin(medecin: any) {
    this.selectedMedecinId = medecin.id;
    this.selectedMedecinName = medecin.username;
    this.patientData.medecin_traitant = medecin.username;  // Met à jour le champ du médecin dans patientData
    this.isListVisible = false;
  }

  // Fonction pour envoyer les données du patient
  onSubmit() {
    if (this.selectedMedecinId !== null) {
      const patientDataToSubmit = {
        ...this.patientData,
        medecin_traitant: this.selectedMedecinId,  // Utilise l'ID du médecin sélectionné
      };

      this.http.post('http://127.0.0.1:8000/patient/', patientDataToSubmit)
        .subscribe(
          response => {
            alert('Dossier patient créé avec succès');
          },
          error => {
            alert('Erreur lors de la création du dossier patient');
          }
        );
    } else {
      alert('Veuillez sélectionner un médecin');
    }
  }
}
