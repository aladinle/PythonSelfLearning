import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LyricSearchComponent } from './lyric-search.component';

describe('LyricSearchComponent', () => {
  let component: LyricSearchComponent;
  let fixture: ComponentFixture<LyricSearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LyricSearchComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LyricSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
