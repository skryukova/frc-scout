import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamReportLinkComponent } from './team-report-link.component';

describe('TeamReportLinkComponent', () => {
  let component: TeamReportLinkComponent;
  let fixture: ComponentFixture<TeamReportLinkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamReportLinkComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamReportLinkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
