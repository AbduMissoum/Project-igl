import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RechercherPatientComponent } from './rechercher-patient.component';

describe('RechercherPatientComponent', () => {
  let component: RechercherPatientComponent;
  let fixture: ComponentFixture<RechercherPatientComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RechercherPatientComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RechercherPatientComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
