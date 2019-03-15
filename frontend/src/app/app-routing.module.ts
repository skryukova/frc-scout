import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CurrentEventComponent } from './current-event/current-event.component'
import { TeamsComponent } from './teams/teams.component'
import { MatchTeamReportComponent } from './match-team-report/match-team-report.component'
import { MatchReportComponent } from './match-report/match-report.component'
import { EventsComponent } from './events/events.component'

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'events',
    component: EventsComponent
  },
  {
    path: 'current-event',
    component: CurrentEventComponent
  },
  {
    path: 'teams',
    component: TeamsComponent
  },
  {
    path: 'report/match/:match/team/:team',
    component: MatchTeamReportComponent
  },  
  {
    path: 'report/event/:event/match/:match',
    component: MatchReportComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
