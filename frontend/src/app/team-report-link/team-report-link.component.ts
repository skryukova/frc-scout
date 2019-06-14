import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-team-report-link',
  templateUrl: './team-report-link.component.html',
  styleUrls: ['./team-report-link.component.scss']
})
export class TeamReportLinkComponent implements OnInit {

  @Input() match_key: string;
  @Input() team_key: string;
  @Input() team_details: Object;
  isDisqualified: Boolean;

  constructor() { }

  ngOnInit() {
    this.isDisqualified = this.team_details["dq_this_match"];
  }

}
