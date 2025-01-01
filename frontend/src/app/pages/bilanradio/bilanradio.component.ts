import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-bilanradio',
  standalone: true,
  templateUrl: './bilanradio.component.html',
   imports: [CommonModule],
  styleUrls: ['./bilanradio.component.css']
})
export class BilanradioComponent {
  title = 'Bilan Radiologique';
  images = [
    { name: 'Radio du thorax', date: '2023-12-01' },
    { name: 'IRM cérébrale', date: '2023-11-20' }
  ];
}
