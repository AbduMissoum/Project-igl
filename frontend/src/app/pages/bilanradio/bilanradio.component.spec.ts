import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BilanradioComponent } from './bilanradio.component';

describe('BilanradioComponent', () => {
  let component: BilanradioComponent;
  let fixture: ComponentFixture<BilanradioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BilanradioComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BilanradioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
