# This file will eventually contain access to the database or another datastore
from flask_restful import Resource
from flask import current_app
from datetime import date
from datetime import datetime


class BaseResource(Resource):
    @property
    def _blue_alliance_api_(self):
        return current_app.config["BLUE_ALLIANCE_API"]

    @property
    def _home_team_key_(self):
        return current_app.config["HOME_TEAM"]

    def get_events(self, team):
        events = self._blue_alliance_api_.get_events(team)
        today = self._blue_alliance_api_.today()
        for event in events:
            start_date = datetime.strptime(event["start_date"], "%Y-%m-%d").date()
            end_date = datetime.strptime(event["end_date"], "%Y-%m-%d").date()
            event["past"] = end_date < today
            event["future"] = start_date > today
            event["current"] = start_date <= today <= end_date
        return events


class Team(BaseResource):
    def get(self, key):
        return self._blue_alliance_api_.get_team(key)


class HomeTeam(BaseResource):
    def get(self):
        return self._blue_alliance_api_.get_team(self._home_team_key_)


class Events(BaseResource):
    def get(self):
        return self.get_events(self._home_team_key_)


class CurrentEvent(BaseResource):
    def get(self):
        events = self.get_events(self._home_team_key_)
        for event in events:
            if event["current"]:
                return event
        return None


class FutureEvents(BaseResource):
    def get(self):
        events = self.get_events(self._home_team_key_)
        future_events = []
        for event in events:
            if event["future"]:
                future_events.append(event)
        return future_events
