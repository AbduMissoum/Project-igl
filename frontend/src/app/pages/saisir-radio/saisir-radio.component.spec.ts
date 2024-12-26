import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SaisirRadioComponent } from './saisir-radio.component';

describe('SaisirRadioComponent', () => {
  let component: SaisirRadioComponent;
  let fixture: ComponentFixture<SaisirRadioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SaisirRadioComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SaisirRadioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
