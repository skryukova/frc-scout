import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MatchTeamReportComponent } from './match-team-report.component';

describe('MatchTeamReportComponent', () => {
  let component: MatchTeamReportComponent;
  let fixture: ComponentFixture<MatchTeamReportComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MatchTeamReportComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MatchTeamReportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
