import json
import os
import requests
from hashlib import md5


class RealBlueAlliance:
    READ_URL_PRE = 'https://www.thebluealliance.com/api/v3'
    session = requests.Session()

    def __init__(self, auth_secret):
        self.auth_secret = auth_secret
        self.session.headers.update({'X-TBA-Auth-Key': auth_secret})

    def _get(self, url):
        return self.session.get(self.READ_URL_PRE + url).json()

    @staticmethod
    def team_key(identifier):
        return identifier if type(identifier) == str else 'frc%s' % identifier

    def status(self):
        return self.get('status')

    def _teams(self, page=None, year=None, simple=False, keys=False):
        if year:
            if page:
                if keys:
                    return self._get('/teams/%d/%d/keys' % (year, page))
                elif simple:
                    return self._get('/teams/%d/%d/simple' % (year, page))
                else:
                    return self._get('/teams/%d/%d' % (year, page))

    def get_team(self, key):
        return self._get('/team/%s' % key)

    def get_match(self, key):
        return self._get('/match/%s' % key)

    def get_events(self, team):
        return self._get('/team/%s/events' % team)

    def get_team_event_matches(self, team, event):
        return self._get('/team/%s/event/%s/matches' % (team, event))

    def get_event_teams_keys(self, event):
        return self._get('/event/%s/teams/keys' % event)

    def get_event_matches(self, event):
        return self._get('/event/%s/matches' % event)

    def get_event_match(self, event, match):
        matches = self._get('/event/%s/matches' % event)
        for game in matches:
            if game["comp_level"] == "qm":
                if game["match_number"] == match:
                    return game

    def get_team_event_status(self, team, event):
        return self._get('/team/%s/event/%s/status' % (team, event))

    def get_event_event_teams_statuses(self, event):
        return self._get('/event/%s/teams/statuses' % event)

