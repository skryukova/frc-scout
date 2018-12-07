import json
import os


class MockBlueAlliance:
    def __init__(self, root=None):
        if root is None:
            self.__root__ = __path__[0]
        else:
            self.__root__ = root

    def __load__(self, file_name):
        file_path = os.path.join(self.__root__, file_name)
        with open(file_path, "rt") as f:
            return json.load(f)

    def get_team(self, key):
        return self.__load__("team.json")[key]

    def get_match(self, key):
        return self.__load__("match.json")[key]

    def get_events(self, team):
        return self.__load__("events.json")[team]

    def get_team_event_matches(self, team, event):
        return self.__load__("team_event_matches.json")[team][event]

    def get_event_teams_keys(self, event):
        return self.__load__("event_teams_keys.json")[event]

    def get_event_matches(self, event):
        return self.__load__("event_matches.json")[event]
    
    def today(self):
        import datetime
        return datetime.datetime.strptime("2018-04-06", "%Y-%m-%d").date()
