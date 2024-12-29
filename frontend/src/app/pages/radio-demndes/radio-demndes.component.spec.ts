import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RadioDemndesComponent } from './radio-demndes.component';

describe('RadioDemndesComponent', () => {
  let component: RadioDemndesComponent;
  let fixture: ComponentFixture<RadioDemndesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RadioDemndesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RadioDemndesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
