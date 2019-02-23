import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DataService } from '../data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  event: JSON;

  home_team$: Object;
  current_event$: Object;

  constructor(private data: DataService, private httpClient : HttpClient) { }

  ngOnInit() {
    this.data.getHomeTeam().subscribe(
      data => this.home_team$ = data 
    );
    this.data.getCurrentEvent().subscribe(
      data => this.current_event$ = data
    );
  }

  getEvent() {
    this.httpClient.get('http://localhost:5000/events').subscribe(data => {
      this.event = data as JSON;
      console.log(this.event);
    })
  }
}
