import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalyseDemandeComponent } from './analyse-demande.component';

describe('AnalyseDemandeComponent', () => {
  let component: AnalyseDemandeComponent;
  let fixture: ComponentFixture<AnalyseDemandeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AnalyseDemandeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AnalyseDemandeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
