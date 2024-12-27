import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private role: string = '';

  setRole(role: string): void {
    this.role = role;
  }

  getRole(): string {
    return this.role;
  }
}
