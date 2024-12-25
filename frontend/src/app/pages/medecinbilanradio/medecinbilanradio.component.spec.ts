import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedecinbilanradioComponent } from './medecinbilanradio.component';

describe('MedecinbilanradioComponent', () => {
  let component: MedecinbilanradioComponent;
  let fixture: ComponentFixture<MedecinbilanradioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MedecinbilanradioComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MedecinbilanradioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
