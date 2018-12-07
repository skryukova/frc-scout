import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Observable } from 'rxjs';
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-match-team-report',
  templateUrl: './match-team-report.component.html',
  styleUrls: ['./match-team-report.component.scss']
})
export class MatchTeamReportComponent implements OnInit {
  report$: Object;
  match$: Object;
  team$: Object;
  event$: Object;
  config$: Object;

  // Parameters:
  match_id$: string;
  team_id$: string;

  constructor(private route: ActivatedRoute, private data: DataService) { 
    this.route.params.subscribe( params => {
      this.match_id$ = params.match,
      this.team_id$ = params.team
    });
  }

  ngOnInit() {
    this.data.getTeam(this.team_id$).subscribe(
      data => this.team$ = data
    );
    this.data.getMatch(this.match_id$).subscribe(
      data => { 
        this.match$ = data;
        this.data.getEventReportConfiguration(data["event_key"]).subscribe(
          data => this.config$ = data
        )
        this.data.getEvent(data["event_key"]).subscribe(
          data => this.event$ = data
        )
      }
    )  
    this.data.getMatchTeamReport(this.match_id$, this.team_id$).subscribe(
      data => this.report$ = data 
    );
  }

}
