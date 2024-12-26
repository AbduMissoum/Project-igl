import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SaisirAnalyseComponent } from './saisir-analyse.component';

describe('SaisirAnalyseComponent', () => {
  let component: SaisirAnalyseComponent;
  let fixture: ComponentFixture<SaisirAnalyseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SaisirAnalyseComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SaisirAnalyseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
