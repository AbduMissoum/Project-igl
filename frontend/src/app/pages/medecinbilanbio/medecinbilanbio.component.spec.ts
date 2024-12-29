import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedecinbilanbioComponent } from './medecinbilanbio.component';

describe('MedecinbilanbioComponent', () => {
  let component: MedecinbilanbioComponent;
  let fixture: ComponentFixture<MedecinbilanbioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MedecinbilanbioComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MedecinbilanbioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
