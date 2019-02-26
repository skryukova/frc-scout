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
    var config = this.http.get(this.env.api_url + "event/" + event + '/config')
    return config;
  }

  getMatchTeamReport(match, team)
  {
    return this.http.get(this.env.api_url + "match/" + match + '/team/' + team)
  }

  getEventMatch(event, match){
    return this.http.get(this.env.api_url + "event/" + event + "/match/" + match)
  }
  updateMatchTeamReport(match, team, report)
  {
    console.log("In updateMatchTeamReport ")
    var data = JSON.stringify(report)
    console.log("Data: " + data) 
    this.http.put(
      this.env.api_url + "match/" + match + '/team/' + team,
      data,
      {}
    ).subscribe(
      data => {
        console.log("Inside subscribe")
      }
    )
    console.log("After updateMatchTeamReport")
  }
}
