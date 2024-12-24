import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsultationSectionComponent } from './consultation-section.component';

describe('ConsultationSectionComponent', () => {
  let component: ConsultationSectionComponent;
  let fixture: ComponentFixture<ConsultationSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConsultationSectionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ConsultationSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
