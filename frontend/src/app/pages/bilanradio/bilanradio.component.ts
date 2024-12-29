import { Component } from '@angular/core';

@Component({
  selector: 'app-bilanradio',
  template: `
  <div class="bg-white p-6 rounded-lg shadow flex space-x-6">
    <div>
      <h2 class="text-2xl font-bold text-fonce">Compte Rendu</h2>
      <p class="mt-4">Texte du compte rendu radiologique...</p>
    </div>
    <img src="assets/images/radio.png" alt="Radiographie" class="w-64 h-64 object-contain">
  </div>
`,
styles: []
})
export class BilanradioComponent {

}
