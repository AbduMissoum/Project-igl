import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PatientSoinComponent } from './patient-soin.component';

describe('PatientSoinComponent', () => {
  let component: PatientSoinComponent;
  let fixture: ComponentFixture<PatientSoinComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PatientSoinComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PatientSoinComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
