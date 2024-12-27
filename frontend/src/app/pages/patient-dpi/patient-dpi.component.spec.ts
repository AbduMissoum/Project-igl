import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PatientDPIComponent } from './patient-dpi.component';

describe('PatientDPIComponent', () => {
  let component: PatientDPIComponent;
  let fixture: ComponentFixture<PatientDPIComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PatientDPIComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PatientDPIComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
