
export interface Soins {
  id: number; // Unique identifier for the soins
  description: string; // Description of the soins or treatment
  la_date: string; // Date of the soins (format: YYYY-MM-DD)
  patient: number; // ID of the patient associated with the soins
  infirmier: number; // ID of the infirmier (nurse) associated with the soins
}

export interface SoinsCreateRequestBody {
  description: string; // Description of the care or treatment
  NSS: string;         // Patient's National Social Security number
  la_date: string;     // Date of the care or treatment (formatted as YYYY-MM-DD)
}






export interface Patient {
  NSS: string; // National Social Security number
  nom: string; // Last name
  prenom: string; // First name
}

export interface Infirmier {
  username: string; // Nurse's username
  email: string;    // Nurse's email
}

export interface SoinsById {
  id: number; // Unique identifier for the record
  patient: Patient; // Patient details
  infirmier: Infirmier; // Nurse details
  description: string; // Description of the case
  la_date: string; // Date of the record
}


export interface SoinListForPatient {
  id: number;
  la_date: string;
  description: string;
  infirmier: Infirmier;
  patient_id: number;
}