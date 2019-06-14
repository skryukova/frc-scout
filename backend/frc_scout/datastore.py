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

    @property
    def _clock_(self):
        return current_app.config["CLOCK"]

    def get_events(self, team):
        events = self._blue_alliance_api_.get_events(team)
        today = self._clock_.today()
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

    def enrich_match(self, match, team_statuses=None):
        """
        Enrich the match data structure (specifically alliances part) with
            1) who the winner is (if known)
            2) current ranking of the teams
            3) # of ranking points received
        :param match: raw match data structure returned from Blue Alliance
        :return:
        """
        # Mark the winning alliance
        match["alliances"]["red"]["winner"] = False
        match["alliances"]["blue"]["winner"] = False
        if match["winning_alliance"] != "":
            match["alliances"][match["winning_alliance"]]["winner"] = True

        # Add ranking points
        if match["score_breakdown"] is not None:
            match["alliances"]["blue"]["rp"] = match["score_breakdown"]["blue"]["rp"]
            match["alliances"]["red"]["rp"] = match["score_breakdown"]["red"]["rp"]

        if team_statuses is None:
            team_statuses = self._blue_alliance_api_.get_event_event_teams_statuses(match["event_key"])

        for alliance in ["blue", "red"]:
            match["alliances"][alliance]["team_details"] = {}
            for team in match["alliances"][alliance]["team_keys"]:
                details = {}
                if team in team_statuses:
                    details = team_statuses[team]["qual"]["ranking"]
                match["alliances"][alliance]["team_details"][team] = details


class ReportConfiguration(BaseResource):
    def get(self, event):
        config = [
            {
                "name": "Auton",
                "type": "string",
                "label": "Auton",
                "control": "select",
                "options": [
                    "No",
                    "Yes",
                    "Somewhat"
                ]
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


class Teams(BaseResource):
    def get(self):
        # First get all events
        current_year = self._clock_.today().year
        current_app.logger.info("Current year: {0}".format(current_year))
        events = self.get_events(self._home_team_key_)
        teams = {}
        for event in events:
            if event["year"] == current_year:
                event_key = event["key"]
                current_app.logger.info("Considering teams for event '{0}'".format(event_key))
                event_teams = self._blue_alliance_api_.get_event_teams_keys(event_key)
                for team in event_teams:
                    if team == self._home_team_key_:
                        continue
                    if team not in teams:
                        teams[team] = []
                    teams[team].append(event_key)
        return teams


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
        team_statuses = self._blue_alliance_api_.get_event_event_teams_statuses(key)
        for match in matches:
            self.enrich_match(match, team_statuses)
        return matches


class EventMatch(BaseResource):
    def get(self, event, match):
        match = self._blue_alliance_api_.get_event_match(event, match)
        self.enrich_match(match)
        return match


class Match(BaseResource):
    def get(self, key):
        match = self._blue_alliance_api_.get_match(key)
        self.enrich_match(match)
        return match


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
