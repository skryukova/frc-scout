# This file will eventually contain access to the database or another datastore
from flask_restful import Resource
from flask import current_app
from flask import request
from datetime import datetime
from os import path
import json


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

    def get_file_path(self, file_name):
        full_path = path.join(current_app.instance_path, file_name)
        return full_path

    def load_file(self, file_name):
        full_path = self.get_file_path(file_name)
        if path.exists(full_path):
            with open(full_path, "rt") as f:
                return json.load(f)
        return {}

    def dump_file(self, obj, file_name):
        full_path = self.get_file_path(file_name)
        with open(full_path, "wt") as f:
            json.dump(obj, f, indent=True)
        return None


class ReportConfiguration(BaseResource):
    def get(self, event):
        config = [
            {
                "name": "Auton",
                "type": "string",
                "label": "Auton",
                "control": "text"
            },
            {
                "name": "NumberOnSwitch",
                "type": "number",
                "label": "# on switch",
                "control": "number"
            },
            {
                "name": "NumberOnScale",
                "type": "number",
                "label": "# on scale",
                "control": "number"
            },
            {
                "name": "NumberInVault",
                "type": "number",
                "label": "# in vault",
                "control": "number"
            },
            {
                "name": "ScoreOnSwitch",
                "type": "boolean",
                "label": "Scored on switch",
                "control": "checkbox"
            },
            {
                "name": "ScoreOnScale",
                "type": "boolean",
                "label": "Scored on scale",
                "control": "checkbox"
            }
        ]
        return config


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


class Event(BaseResource):
    def get(self, key):
        events = self.get_events(self._home_team_key_)
        for event in events:
            if event["key"] == key:
                return event
        return None


class EventMatches(BaseResource):
    def get(self, key):
        matches = self._blue_alliance_api_.get_event_matches(key)
        return matches


class Match(BaseResource):
    def get(self, key):
        return self._blue_alliance_api_.get_match(key)


class TeamMatchReport(BaseResource):
    def get_file_name(self, match, team):
        return "{0}_{1}.json".format(match, team)

    def get(self, match, team):
        return self.load_file(self.get_file_name(match, team))

    def put(self, match, team):
        current_app.logger.info("JSON: {0}".format(request.json))
        current_app.logger.info("DATA: {0}".format(request.data))
        if request.json is None:
            data = json.loads(request.data)
        else:
            data = request.json
        return self.dump_file(
            data,
            self.get_file_name(match, team))
