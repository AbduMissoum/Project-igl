import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AdminPageComponent } from './pages/admin-page/admin-page.component';

@Component({
  selector: 'app-root',
  imports: [ AdminPageComponent ],
  templateUrl: './app.component.html',  // Vérifie que ton template a bien le <router-outlet>
})
export class AppComponent {
  title = 'frontend';
}
