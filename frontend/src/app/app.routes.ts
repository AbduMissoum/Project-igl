
import { Routes } from '@angular/router';
import { SaisirSoinComponent } from './pages/saisir-soin/saisir-soin.component';
import { ContactComponent } from './pages/contact/contact.component';
import { SaisirRadioComponent } from './pages/saisir-radio/saisir-radio.component';
import { LoginComponent } from './pages/login/login.component';
import { AdminPageComponent } from './pages/admin-page/admin-page.component';
import { AnalyseDemandeComponent } from './pages/analyse-demande/analyse-demande.component';
import { MedecinComponent } from './pages/medecin/medecin.component';
import { PatientresumeComponent } from './pages/patientresume/patientresume.component';
import { RadioDemndesComponent } from './pages/radio-demndes/radio-demndes.component';
import { SaisirAnalyseComponent } from './pages/saisir-analyse/saisir-analyse.component';

export const routes: Routes = [ 
    {
        path: '',
        redirectTo: 'login',
        pathMatch :'full'  , 
      },
      {
        path: 'login',
        component: LoginComponent, // Redirige vers la page par défaut si aucune route ne correspond
      },
      {
        path: 'contactus',
        component: ContactComponent, 
      },
      {
      path: 'admin',
      component: AdminPageComponent, 
         },
     {
            path: 'analysedemande',
            component: AnalyseDemandeComponent, 
          },
       
          
       {
        path: 'medecin',
        component: MedecinComponent, 
      },
      {
        path: 'patient',
        component: PatientresumeComponent, 
      },
      {
        path: 'radiodemande',
        component: RadioDemndesComponent, 
      },
      {
        path: 'saisiranalyse',
        component: SaisirAnalyseComponent, 
      },
      {
        path: 'saisirradio',
        component: SaisirRadioComponent, 
      },
      {
        path: 'saisirsoin',
        component: SaisirSoinComponent, 
      },

      ];

