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

  getTeam(team) {
    return this.http.get(this.env.api_url + 'team/' + team)
  }

  getCurrentEvent() {
    return this.http.get(this.env.api_url + 'events/current')
  }

  getEvent(event) {
    return this.http.get(this.env.api_url + "event/" + event )  
  }

  getEventMatches(event) {
    return this.http.get(this.env.api_url + "event/" + event + '/matches')
  }

  getMatch(match) {
    return this.http.get(this.env.api_url + "match/" + match)
  }

  getEventReportConfiguration(event)
  {
    return this.http.get(this.env.api_url + "event/" + event + '/config')
  }

  getMatchTeamReport(match, team)
  {
    return this.http.get(this.env.api_url + "match/" + match + '/team/' + team)
  }
}
