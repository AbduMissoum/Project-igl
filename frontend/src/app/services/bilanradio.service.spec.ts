import { TestBed } from '@angular/core/testing';

import { BilanradioService } from './bilanradio.service';

describe('BilanradioService', () => {
  let service: BilanradioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BilanradioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
