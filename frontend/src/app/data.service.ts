import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  env = environment;

  constructor(private http: HttpClient) { }

  getHomeTeam() {
    return this.http.get(this.env.api_url + 'home')
  }

  getCurrentEvent() {
    return this.http.get(this.env.api_url + 'events/current')
  }

  getEventMatches(event) {
    return this.http.get(this.env.api_url + "event/" + event + '/matches')
  }
}
