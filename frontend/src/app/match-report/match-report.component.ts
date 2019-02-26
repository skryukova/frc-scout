import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

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
  current_event$: Object;

  // Parameters:
  event_id$: string;
  match_id$: string;

  constructor(private httpClient: HttpClient, private route: ActivatedRoute, private data: DataService) {
    this.route.params.subscribe( params => {
      this.event_id$ = params.event,
      this.match_id$ = params.match
    });
   }

  ngOnInit() {
    this.data.getEventMatch(this.event_id$, this.match_id$).subscribe(
      data => { 
        this.match$ = data;
      }
    )
    // This does not actually work completely right, it just sort of works, yah no more questions thank you.
    this.httpClient.get('http://localhost:5000/events/current').subscribe(data => {
      this.current_event$ = data;
    })
  }


}
