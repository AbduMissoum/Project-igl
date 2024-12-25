import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrdonanceComponent } from './ordonance.component';

describe('OrdonanceComponent', () => {
  let component: OrdonanceComponent;
  let fixture: ComponentFixture<OrdonanceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OrdonanceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OrdonanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
