import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CurrentEventComponent } from './current-event/current-event.component'
import { TeamsComponent } from './teams/teams.component'
import { MatchTeamReportComponent } from './match-team-report/match-team-report.component'
import { MatchReportComponent } from './match-report/match-report.component'

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
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
    path: 'report/:match/:team',
    component: MatchTeamReportComponent
  },
  {
    path: 'report/:match',
    component: MatchReportComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
