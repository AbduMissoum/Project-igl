import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BilanbioComponent } from './bilanbio.component';

describe('BilanbioComponent', () => {
  let component: BilanbioComponent;
  let fixture: ComponentFixture<BilanbioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BilanbioComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BilanbioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
