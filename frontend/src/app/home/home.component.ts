import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  event: JSON;

  constructor(private httpClient: HttpClient) { }

  ngOnInit() {
  }

  getEvent() {
    this.httpClient.get('http://localhost:5000/events').subscribe(data => {
      this.event = data as JSON;
      console.log(this.event);
    })
  }
}
