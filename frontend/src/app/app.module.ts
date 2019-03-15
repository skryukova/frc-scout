import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { MatButtonModule, MatCheckboxModule, MatSidenavModule, MatToolbarModule } from '@angular/material';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { HomeComponent } from './home/home.component';
import { CurrentEventComponent } from './current-event/current-event.component';
import { TeamsComponent } from './teams/teams.component';
import { MatchTeamReportComponent } from './match-team-report/match-team-report.component';
import { MatchReportComponent } from './match-report/match-report.component';
import { EventsComponent } from './events/events.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    HomeComponent,
    CurrentEventComponent,
    TeamsComponent,
    MatchTeamReportComponent,
    MatchReportComponent,
    EventsComponent
  ],
  imports: [
    NoopAnimationsModule,
    MatButtonModule,
    MatCheckboxModule,
    MatSidenavModule,
    MatToolbarModule,
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
