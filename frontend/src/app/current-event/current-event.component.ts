import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-current-event',
  templateUrl: './current-event.component.html',
  styleUrls: ['./current-event.component.scss']
})
export class CurrentEventComponent implements OnInit {

  currentEvent : JSON;

  constructor(private httpClient : HttpClient) { }

  ngOnInit() {
  }
  
  getCurrentEvent() {
    this.httpClient.get('http://localhost:5000/events/current').subscribe(data => {
      this.currentEvent = data as JSON;
      console.log(this.currentEvent);
    })
  }

}
