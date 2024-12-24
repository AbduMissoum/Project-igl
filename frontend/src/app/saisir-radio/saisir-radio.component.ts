import { Component , ViewChild , ElementRef } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-saisir-radio',
  imports: [FormsModule , CommonModule],
  templateUrl: './saisir-radio.component.html',
  styleUrl: './saisir-radio.component.css'
})
export class SaisirRadioComponent {
  file: File | null = null;
@ViewChild('fileInput', { static: false })
fileInput!: ElementRef<HTMLInputElement>;
compteRendu: string = ''; 
isInvalid: boolean = false;



  onDragOver(event: DragEvent) {
    event.preventDefault();
    const uploadSection = event.target as HTMLElement;
    uploadSection.classList.add('dragover');
  }

  onDragLeave(event: DragEvent) {
    const uploadSection = event.target as HTMLElement;
    uploadSection.classList.remove('dragover');
  }

  onFileDrop(event: DragEvent) {
    event.preventDefault();
    const uploadSection = event.target as HTMLElement;
    uploadSection.classList.remove('dragover');
    if (event.dataTransfer && event.dataTransfer.files.length > 0) {
      this.file = event.dataTransfer.files[0];
      console.log('File dropped:', this.file);
    }
  }
  triggerFileInput(): void {
    this.fileInput.nativeElement.click(); 
  }

  onFileSelect(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.file = input.files[0];
      console.log('File selected:', this.file);
    }
    
  }

  onRetour() {
    console.log('Retour');
  }

  onEnvoyer() {


    if (!this.compteRendu.trim()) {
      this.isInvalid = true; 
    } else {
      this.isInvalid = false; 
      console.log('Compte rendu envoyé:', this.compteRendu);
    }
    if (this.file) {
      console.log('File to upload:', this.file);
    } else {
      console.log('No file selected.');
    }
    console.log('Compte rendu envoyé.');
  }

}




