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

    def __get_by_key__(self, file_name, key, random=False):
        values_dict = self.__load__(file_name)
        if key in values_dict:
            return values_dict[key]
        if random:
            if len(values_dict) > 0:
                for k in values_dict:
                    return values_dict[k]
        return None

    def get_team(self, key):
        return self.__get_by_key__("team.json", key, random=True)

    def get_match(self, key):
        return self.__get_by_key__("match.json", key, random=True)

    def get_events(self, team):
        return self.__load__("events.json")[team]

    def get_team_event_matches(self, team, event):
        return self.__load__("team_event_matches.json")[team][event]

    def get_event_teams_keys(self, event):
        return self.__load__("event_teams_keys.json")[event]

    def get_event_matches(self, event):
        return self.__load__("event_matches.json")[event]

    def get_event_match(self, event, match):
        file = self.__load__("event_matches.json")[event]
        for game in file:
            if game["match_number"] == match:
                if game["comp_level"] == "qm":
                    return game
