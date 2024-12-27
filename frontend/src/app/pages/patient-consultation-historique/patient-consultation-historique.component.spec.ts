import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PatientConsultationHistoriqueComponent } from './patient-consultation-historique.component';

describe('PatientConsultationHistoriqueComponent', () => {
  let component: PatientConsultationHistoriqueComponent;
  let fixture: ComponentFixture<PatientConsultationHistoriqueComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PatientConsultationHistoriqueComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PatientConsultationHistoriqueComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
