import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedecinresumeComponent } from './medecinresume.component';

describe('MedecinresumeComponent', () => {
  let component: MedecinresumeComponent;
  let fixture: ComponentFixture<MedecinresumeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MedecinresumeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MedecinresumeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
