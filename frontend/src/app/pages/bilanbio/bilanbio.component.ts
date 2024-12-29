import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-bilanbio',
  standalone: true,
  templateUrl: './bilanbio.component.html',
  imports: [CommonModule],
  styleUrls: ['./bilanbio.component.css']
})
export class BilanbioComponent {
  title = 'Bilan Biologique';
  bioResults = [
    { test: 'Glucose', value: '5.2', unit: 'mmol/L', reference: '4.0 - 6.0' },
    { test: 'Cholestérol', value: '4.8', unit: 'mmol/L', reference: '< 5.0' }
  ];
}
