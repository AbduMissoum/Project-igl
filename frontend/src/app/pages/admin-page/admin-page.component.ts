import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-admin-page',
  templateUrl: './admin-page.component.html',
  imports: [CommonModule, FormsModule],
  styleUrls: ['./admin-page.component.css'],
})
export class AdminPageComponent implements OnInit {
  // Variables pour gérer les médecins et leur filtrage
  medecins: any[] = [];
  filteredMedecins: any[] = [];
  selectedMedecins: any[] = []; // Tableau pour stocker les médecins sélectionnés
  isListVisible: boolean = false;

  

  patientData = {
    NSS: '',
    nom: '',
    prenom: '',
    date_naissance: '',
    adress: '',
    tel: '',
    mutuelle: '',
    email: '',
    medecin_traitant: [] as number[],  // Tableau pour les IDs des médecins sélectionnés
  };

  swalOptions = {
    customClass: {
      popup: 'rounded-[40px] shadow-lg bg-clair p-6 text-center', // Style du popup
      title: 'text-2xl font-bold text-fonce', // Style du titre
      confirmButton: 'bg-fonce text-white w-auto px-8 rounded-[40px]', // Style du bouton de confirmation
      cancelButton: 'bg-gray-200 text-fonce px-8 rounded-[40px]', // Style du bouton d'annulation
    },
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
      });
  }

  // Fonctions pour gérer l'affichage de la liste des médecins
  showList() {
    this.isListVisible = true;
  }

  hideList() {
    setTimeout(() => {
      this.isListVisible = false; // Utiliser un timeout pour laisser le clic se terminer avant de cacher
    }, 200);
  }

  // Fonction pour filtrer la liste des médecins selon l'input utilisateur
  filterMedecins(event: any) {
    const query = event.target.value.toLowerCase();
    this.filteredMedecins = this.medecins.filter((medecin) =>
      medecin.username.toLowerCase().includes(query)
    );
  }

  // Fonction pour ajouter un médecin à la sélection
  selectMedecin(medecin: any) {
    if (!this.selectedMedecins.some((selected) => selected.id === medecin.id)) {
      this.selectedMedecins.push(medecin); // Ajoute l'objet médecin à la liste des médecins sélectionnés
      this.patientData.medecin_traitant.push(medecin.id);  // Ajoute l'ID du médecin au tableau
    }
    this.isListVisible = false; // Masque la liste après sélection
  }

  // Fonction pour supprimer un médecin de la sélection
  removeMedecin(index: number) {
    const removedMedecin = this.selectedMedecins.splice(index, 1)[0];
    const medecinIndex = this.patientData.medecin_traitant.indexOf(removedMedecin.id);
    if (medecinIndex !== -1) {
      this.patientData.medecin_traitant.splice(medecinIndex, 1); // Retirer l'ID du tableau
    }
  }

  // Fonction pour envoyer les données du patient
  onSubmit() {
    Swal.fire({
      ...this.swalOptions, // Ajout du style global
      title: 'Êtes-vous sûr ?',
      text: "Vous êtes sur le point de valider les informations du patient.",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Oui, envoyer !',
    }).then((result) => {
      if (result.isConfirmed) {
        // Soumission des données
        if (this.patientData.medecin_traitant.length > 0) {
          const patientDataToSubmit = {
            ...this.patientData,
          };
          this.http.post('http://127.0.0.1:8000/patient/', patientDataToSubmit)
            .subscribe(
              response => {
                Swal.fire({
                  ...this.swalOptions,  // Ajout du style global
                  title: 'Succès',
                  text: 'Dossier patient créé avec succès',
                  icon: 'success',
                });
              },
              error => {
                console.error('Erreur lors de la création :', error);
                Swal.fire({
                  ...this.swalOptions,  // Ajout du style global
                  title: 'Erreur',
                  text: 'Une erreur est survenue lors de la création du dossier',
                  icon: 'error',
                });
              }
            );
        } else {
          Swal.fire({
            ...this.swalOptions,  // Ajout du style global
            title: 'Attention',
            text: 'Veuillez sélectionner au moins un médecin',
            icon: 'warning',
          });
        }
      }
    });
  }
  
}
