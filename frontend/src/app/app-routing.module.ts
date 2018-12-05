import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CurrentEventComponent } from './current-event/current-event.component'

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'current-event',
    component: CurrentEventComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
