import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Observable } from 'rxjs';
import { filter } from 'rxjs/operators';

interface Match {
  comp_level: string,
  match_number: number
}

@Component({
  selector: 'app-current-event',
  templateUrl: './current-event.component.html',
  styleUrls: ['./current-event.component.scss']
})
export class CurrentEventComponent implements OnInit {
  current_event$: Object;
  matches$: Object = null;
  qualifyingMatches: Object = null;

  constructor(private data: DataService) { }

  ngOnInit() {
    this.data.getCurrentEvent().subscribe(
      data => { 
        this.current_event$ = data;
        this.data.getEventMatches(data["key"]).subscribe(
          data => this.matches$ = data
        )
      }
    );
  }

  getQualifyingMatches() {
    if (this.matches$ != null) {
      if (this.qualifyingMatches == null) {
        var matchesArray = this.matches$ as Array<Match>;        
        this.qualifyingMatches = matchesArray.filter(
          match => match.comp_level == "qm"
        ).sort(
          (m1, m2) => m1.match_number - m2.match_number
        )
      }
    }
    return this.qualifyingMatches
  }

}
