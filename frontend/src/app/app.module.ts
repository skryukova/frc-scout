import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { HomeComponent } from './home/home.component';
import { CurrentEventComponent } from './current-event/current-event.component';
import { TeamsComponent } from './teams/teams.component';

import { HttpClientModule } from '@angular/common/http';
import { MatchTeamReportComponent } from './match-team-report/match-team-report.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    HomeComponent,
    CurrentEventComponent,
    TeamsComponent,
    MatchTeamReportComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
