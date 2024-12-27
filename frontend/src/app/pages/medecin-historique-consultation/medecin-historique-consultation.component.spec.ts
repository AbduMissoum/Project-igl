import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedecinHistoriqueConsultationComponent } from './medecin-historique-consultation.component';

describe('MedecinHistoriqueConsultationComponent', () => {
  let component: MedecinHistoriqueConsultationComponent;
  let fixture: ComponentFixture<MedecinHistoriqueConsultationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MedecinHistoriqueConsultationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MedecinHistoriqueConsultationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
