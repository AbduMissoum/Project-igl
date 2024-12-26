import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SaisirSoinComponent } from './saisir-soin.component';

describe('SaisirSoinComponent', () => {
  let component: SaisirSoinComponent;
  let fixture: ComponentFixture<SaisirSoinComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SaisirSoinComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SaisirSoinComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
