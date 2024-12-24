import { RouterModule } from '@angular/router';
import { routes } from './app.routes';
import { importProvidersFrom } from '@angular/core';

export const appConfig = {
  providers: [
    importProvidersFrom(RouterModule.forRoot(routes))
  ],
};
