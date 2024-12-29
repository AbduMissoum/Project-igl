import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PatientresumeComponent } from './patientresume.component';

describe('PatientresumeComponent', () => {
  let component: PatientresumeComponent;
  let fixture: ComponentFixture<PatientresumeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PatientresumeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PatientresumeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
