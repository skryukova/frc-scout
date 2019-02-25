import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-match-report',
  templateUrl: './match-report.component.html',
  styleUrls: ['./match-report.component.scss']
})
export class MatchReportComponent implements OnInit {
  report$: Object;
  match$: Object;
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
  }

  getEventInfo(){
    return event;
  }

}
