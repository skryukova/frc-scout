import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CurrentEventComponent } from './current-event/current-event.component'
import { TeamsComponent } from './teams/teams.component'

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
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
