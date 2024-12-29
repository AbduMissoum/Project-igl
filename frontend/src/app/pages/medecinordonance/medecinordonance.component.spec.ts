import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedecinordonanceComponent } from './medecinordonance.component';

describe('MedecinordonanceComponent', () => {
  let component: MedecinordonanceComponent;
  let fixture: ComponentFixture<MedecinordonanceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MedecinordonanceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MedecinordonanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
